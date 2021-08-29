//Navbar

$(function() {
    var navbar = $("#page-navbar");
    //var top = navbar.offset().top;

    // Prevent base navbar from being loaded on a refresh
    if ($(window).scrollTop() > 0) {
        navbar.addClass("scrolled");
        navbar.removeClass("base");
    }
  
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        //console.log(top);

        if (scroll > 20) {
            navbar.addClass("scrolled");
            navbar.removeClass("base");
        } 
        else {
            navbar.removeClass("scrolled");
            navbar.addClass("base");
            //top = navbar.offset().top;
        }
    });
});