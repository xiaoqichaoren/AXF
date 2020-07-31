$(function(){

    initTopSwiper();

    initMenuSwiper();

})


function initTopSwiper(){

    var swiper = new Swiper("#topSwiper", {
        loop: true,
        autoplay: 3000,
        pagination:".swiper-pagination",
        autoloop: 4000
    })
}


function initMenuSwiper(){

    var swiper = new Swiper("#swiperMenu", {
        slidesPerView: 3
    })
}