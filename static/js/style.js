 // transparent navbar turns white when scrolling down
// And returns transparent when is at the top of the screen
$(function () {
    $(window).on('scroll', function () {
        if ( $(window).scrollTop() > 10 ) {
            $('.navbar').addClass('active');
            $('img.nav_logo').attr('src','/static/images/5.png');
        } else {
            $('.navbar').removeClass('active');
            $('img.nav_logo').attr('src','/static/images/4.png');
        }
    });
});


