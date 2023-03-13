# Vehicle Company Business Web Application

#### Video Demo: https://youtu.be/Rc7sm6PXM30

#### Year: 2022

### Description:

The project is a web app where users can choose a vehicle and pre-order the vehicle. I wanted to make a project like this to expand my knowledge of web design. I wanted to make this site very attractive and very user-friendly. Not only that, but I think I got success. I named the company "infinity" and I also designed a logo for the company. The application is fully responsive.

When you arrive at the homepage of this website, you can see a basic description of the company and what the web page does. In the middle of the page, there is a testimonial section that depicts user experience with the business. You can get a pretty good idea about the site and the company from the first page.

On the second-page vehicles page, you can see the company's vehicle gallery. You can choose a vehicle from there. But still, you cannot pre-order as you aren't logged in. When you click on a vehicle on that page, you will be redirected to the login.

The third section is also a login required section. You can pre-order from there also.

Next one is the about us section. If you want to know about the history of the company, your destination should be there. You can see the certificates the company got in there.

If you want to register, you have to go to the register tab and fill out the form. The form is validated through the backend and front end. You have to enter a password with more than 6 characters, including capitals, include numbers, and signs.

After registration, you can log in.

The first impression after login is the portfolio page, which depicts Your buying details and account details.

After you logged in, the order now the tab is available. You can pre-order a vehicle that cost $2000.

After you logged in, you can see a new history tab appears. What it does is it depicts your buying history with a full detailed list.

So there are 11 templates, including apalogy.html.(Which is called When the user inputs something inappropriate. )

### Technologies used:

- HTML
- CSS
- JavaScript
- Python
- Flask
- SQL
- Other small libraries or packages


### How does the webpage work?

The idea is simple. The user can take a look at the vehicle gallery and some other company-related things, but if they want to pre-order a vehicle, they have to get registered on the website. During registration, you need to enter these fields:

- Email
- Username
- Password

When a user get register she/he owns $10, 000 .

The registration allows you to access your dashboard, where you can see what you had been pre-ordering and some other details. Through the history tab, you can take a look at your ordering history.

To pre-order, you have to fill the form in the order-now tab and when you submit the form charges will be applied and your account balance will reduce according to it. Normally, pre-ordering process cost $2, 000.

### Validation

All the registration and login data will be validated through the backend and frontend.



### Database

The database stores all user's data inside two tables. Registration and login data will be stored in users table and all the buying details are stored in the transaction table.

### Possible Improvements

Have an administrator account which confirms user identity, so that fake accounts could not register.

### How to run the app?

- You can type `flask run` in the terminal and the app will be executed.
