$(function () {
    $('.home').width(innerWidth)

    var topSwiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
        autoplay: 3000,
        effect: 'coverflow',
    });


    var mustbuySwiper = new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 5,
        loop: true,
    });
})