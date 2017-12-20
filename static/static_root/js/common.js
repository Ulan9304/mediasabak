$(function () {

    $('.slider').slick({
        cssEase: 'ease-in',
        dots: false,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: true
    });


    $('.tabs-stage > div').hide();
    $('.tabs-stage > div:nth-child(1)').show();
    $('.tabs-nav > li:first-child a').addClass('tab-active');

    $('.tabs-nav > li > a').on('click', function (event) {
        event.preventDefault();
        $('.tabs-nav > li a').removeClass('tab-active');
        $(this).addClass('tab-active');
        $('.tabs-stage > div').hide(500);
        $($(this).attr('href')).show(500);
    });

    $('.list_lesson').perfectScrollbar();
    $('.vid-list-container').perfectScrollbar();

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].onclick = function () {
            this.classList.toggle("active_accordion");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        }
    }


    var description = $('.vid-list > .vid-item');
    description.each(function (i, obj) {
        $(obj).on('click', function (event) {
            var v_desc = $(this).children('.desc').text();
            $('.vid-container > h4').text(v_desc);
        });
    });

    $('.false').click(function () {
        $(this).css('background-color', '#ff7058');
        $('.test_overlay').css('opacity', '1');
    });

    $('.true').click(function () {
        $(this).css('background-color', '#70d958');
        $('.test_overlay').css('opacity', '1');
    });

    $(".hamburger_collapsed").click(function () {
        // alert('hello');
        $('.list_video').toggleClass("hamburger_block");
        $('.video_container .vid-list-container').toggleClass("hamburger_block2");
        $(this).toggleClass("hamburger-expanded");
    });




    new WOW().init();


});