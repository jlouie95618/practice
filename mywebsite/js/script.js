var _MILLISEC_IN_SEC = 1000;
var _NUM_SEC = 1;

$(document).ready(function() {

    var sidebarToggle = true;

    $('.button').click(function() {
        if (sidebarToggle) {
            $('.sidebar.blog').animate({ left: 0 }, 1000);
            $('.wrapper.blog').css({ 'webkit-transform': 'translate(100px, 0px)' });
            sidebarToggle = false;
        } else { 
            $('.sidebar.blog').animate({ left: -200 }, 1000);
            $('.wrapper.blog').css({ 'webkit-transform': 'translate(0px, 0px)' });
            sidebarToggle = true;
        }
    });

    // Code pertaining to the in blog page dropdown...
    $('.blog-archive').hide();
    $('.blog-topics').hide();
    $('.blog-about').hide();
    $('.page-header.blog').hover(function(eventData) {
        $('.blog-archive').stop();
        $('.blog-topics').stop();
        $('.blog-about').stop();
        $('.blog-archive').fadeIn(_MILLISEC_IN_SEC * _NUM_SEC);
        $('.blog-topics').fadeIn(_MILLISEC_IN_SEC * _NUM_SEC);
        $('.blog-about').fadeIn(_MILLISEC_IN_SEC * _NUM_SEC);
        $('.stylized-l-under-title').css({'-webkit-transform' : 'translate(0px, -10px)'});
    }, function(eventData) {
        $('.blog-archive').stop();
        $('.blog-topics').stop();
        $('.blog-about').stop();
        $('.blog-archive').fadeOut(_MILLISEC_IN_SEC * _NUM_SEC);
        $('.blog-topics').fadeOut(_MILLISEC_IN_SEC * _NUM_SEC);
        $('.blog-about').fadeOut(_MILLISEC_IN_SEC * _NUM_SEC);
        $('.stylized-l-under-title').css({'-webkit-transform' : 'translate(0px, 10px)'});
    });

});

function headerOptionFadeIn (elem) {
    elem.stop();
    elem.fadeIn(_MILLISEC_IN_SEC * _NUM_SEC);
}

function headerOptionFadeOut (elem) {
    elem.stop();
    elem.fadeOut(_MILLISEC_IN_SEC * _NUM_SEC);
}