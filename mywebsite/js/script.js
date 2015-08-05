var _MILLISEC_IN_SEC = 1000;
var _NUM_SEC = 1;

$(document).ready(function() {


    $('.button.sidebar-close.hvr-grow').hover(function(eventData) {
        $('.menu-horizontal-bar.top').stop();
        $('.menu-horizontal-bar.bottom').stop();
        $('.menu-horizontal-bar.top').addClass('is-active');
        $('.menu-horizontal-bar.bottom').addClass('is-active');
    }, function(eventData) {
        $('.menu-horizontal-bar.top').stop();
        $('.menu-horizontal-bar.bottom').stop();
        $('.menu-horizontal-bar.top').removeClass('is-active');
        $('.menu-horizontal-bar.bottom').removeClass('is-active');
    });

    $('.button.sidebar-open').click(function() {
        $('.sidebar.blog').stop(true);
        $('.wrapper.blog').stop(true);
        $('.button.sidebar-open').stop(true);
        $('.sidebar.blog').animate({ left: 0 }, 1000);
        $('.wrapper.blog').animate({ 'marginLeft': '435' }, 1000); // 435 === +=100
        $('.button.sidebar-open').fadeOut(500);
    });

    $('.button.sidebar-close').click(function() {
        $('.sidebar.blog').stop(true);
        $('.wrapper.blog').stop(true);
        $('.button.sidebar-open').stop(true);
        $('.sidebar.blog').animate({ left: -200 }, 1000);
        $('.wrapper.blog').animate({ 'marginLeft': '335' }, 1000); // 335 === -=100
        $('.button.sidebar-open').delay(1000).fadeIn('fast');
        sidebarToggle = true;
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