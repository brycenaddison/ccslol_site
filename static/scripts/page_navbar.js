//Navbar

$(function() {
    var navbar = $("#page-navbar");
    //var top = navbar.offset().top;
  
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();

        //console.log(top);

        if (scroll > 25) {
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