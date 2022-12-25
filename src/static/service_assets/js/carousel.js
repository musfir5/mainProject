
$(document).ready(function () {
    var owl = $('.our-work-section .owl-carousel');
    owl.owlCarousel({
        margin: 30,
        nav: true,
        loop: true,
        pagination: true,
        dots:true,
        autoplay:false,
        autoplayTimeout: 4500,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    })
})

$(document).ready(function () {
    var owl = $('.carousel-section .owl-carousel');
    owl.owlCarousel({
        margin: 30,
        nav: true,
        loop: true,
        pagination: true,
        dots:false,
        autoplay:false,
        autoplayTimeout: 4500,
        responsive: {
            0: {
                items: 1
            },
            576: {
                items: 1
            },
            992: {
                items: 1
            }
        }
    })
})