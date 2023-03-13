import os
import datetime
import re
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///infinity_users_log.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    cars = [
        "Koenigsegg Agera R",
        "Pagini Huayra",
        "Bugatti Veyron Super Sports",
        "Lamborghini Aventador",
        "Porsche 918 Spyder Concept",
        "McLaren MP4-12C",
        "Lexus LFA",
        "Mercedes-Benz Sl 65 AMG",
        "Shelby Cobra 427",
    ]
    if request.method == "GET":
        return render_template("orderNow.html", cars=cars)

    else:
        cars = request.form.get("cars")
        shares = 1

        if cars == None:
            return apology("Input Field is Missing")
        else:
            transaction_value = 2000
            user_id = session["user_id"]
            user_cash_db = db.execute(
                "SELECT cash FROM users WHERE id = :user_id", user_id=user_id
            )
            user_cash = float(user_cash_db[0]["cash"])

            if user_cash < transaction_value:
                return apology("Insufficient balance.")
            else:
                update_cash = user_cash - transaction_value
                date_time = datetime.datetime.now()
                price_usd = usd(transaction_value)

                db.execute(
                    "UPDATE users SET cash = ? WHERE id = ?", update_cash, user_id
                )
                db.execute(
                    "INSERT INTO transactions (user_id, symbol, shares, price, date) VALUES(?, ?, ?, ?, ?)",
                    user_id,
                    cars,
                    shares,
                    price_usd,
                    date_time,
                )

                flash("Congratulations car pre ordered!!")

                return redirect("/index")


@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]
    user_details = db.execute("SELECT * FROM transactions WHERE user_id=?", user_id)
    price = user_details
    return render_template("history.html", user_details=user_details)


@app.route("/login", methods=["GET", "POST"])
def login():

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/index")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    else:
        username = request.form.get("full_name")
        password = request.form.get("password")
        confirmation = request.form.get("confirm_password")

        if not username or not password or not confirmation:
            return apology("Input field is missing !!")

        else:

            if password != confirmation:
                return apology("Password does not match !!")
            #
            #     # validate password
            # if len(password) < 8:
            #     return apology("Password must at least have 8 characters")
            # if re.search("[0-9]", password) is None:
            #     return apology("Password must include numbers")
            # if re.search("[A-Z]", password) is None:
            #     return apology("Password must include capital letters")

            else:
                try:
                    hash1 = generate_password_hash(password)
                    db.execute(
                        "INSERT INTO users (username, hash) VALUES(?, ?)",
                        username,
                        hash1,
                    )
                    rows = db.execute(
                        "SELECT * FROM users WHERE username = ?", username
                    )

                    session["user_id"] = rows[0]["id"]
                    return redirect("/index")

                except:
                    return apology("Username Already Exist")


@app.route("/vehicles", methods=["GET", "POST"])
def vehicles():

    return render_template("vehicales.html")


@app.route("/aboutus", methods=["GET", "POST"])
def aboutus():

    return render_template("aboutUs.html")


@app.route("/index")
@login_required
def home():

    """Show portfolio of owned cars"""

    user_id = session["user_id"]

    details = db.execute(
        "SELECT symbol, SUM(shares) AS shares FROM transactions"
        " WHERE user_id = ? GROUP BY symbol",
        user_id,
    )
    if not details:
        details = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        grand_tot = []
        liquid_cash = float(details[0]["cash"])
        details[0]["cash"] = usd(liquid_cash)
        grand_tot.append(liquid_cash)
        sum_grand_tot = sum(grand_tot)
        details[0]["grand_tot"] = usd(sum_grand_tot)

    else:
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        liquid_cash = float(cash[0]["cash"])
        grand_tot = []

        for i in range(len(details)):
            price = 2000
            tot = float(details[i]["shares"]) * price

            grand_tot.append(tot)

            details[i]["price"] = usd(price)
            details[i]["tot"] = usd(tot)

        details[0]["cash"] = usd(liquid_cash)
        grand_tot.append(liquid_cash)
        sum_grand_tot = sum(grand_tot)
        details[0]["grand_tot"] = usd(sum_grand_tot)

    return render_template("logmain.html", details=details)
