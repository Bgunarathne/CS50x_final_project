var navbar = document.querySelector(".navbar");


window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.documentElement.scrollTop > 0) {
    navbar.classList.add("bg-white");
      navbar.classList.remove("navbar-dark");
  } else if(document.documentElement.scrollTop == 0) {
    if($(window).width() > 991){
    navbar.classList.remove("bg-white");
    navbar.classList.add("navbar-dark");
  }
  }
  else{
    navbar.classList.remove("bg-white");
    navbar.classList.add("navbar-dark");
  }
}

window.onresize = function() {myFunction2()};

function  myFunction2(){
    var w =parseFloat( $(window).width());

    if (w < 992) {
        navbar.classList.add("bg-white");
          navbar.classList.remove("navbar-dark");
    }
    else{
      navbar.classList.remove("bg-white");
        navbar.classList.add("navbar-dark");
    }
  }

  var w = $(window).width();

  if (w < 992) {
      navbar.classList.add("bg-white");
        navbar.classList.remove("navbar-dark");}
