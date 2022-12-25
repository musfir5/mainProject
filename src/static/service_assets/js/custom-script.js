
// video popup

$(function () {
  $('.popup-vimeo').magnificPopup({
      disableOn: 700,
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false
  });
});

// count
$(document).ready(function () {

  $('.about-us-section .counter').each(function () {
      $(this).prop('Counter', 0).animate({
          Counter: $(this).text()
      }, {
          duration: 4000,
          easing: 'swing',
          step: function (now) {
              $(this).text(Math.ceil(now));
          }
      });
  });
  
  });

  $(document).ready(function () {

      $('.about-us-section-page .counter').each(function () {
          $(this).prop('Counter', 0).animate({
              Counter: $(this).text()
          }, {
              duration: 4000,
              easing: 'swing',
              step: function (now) {
                  $(this).text(Math.ceil(now));
              }
          });
      });
      
      });
       
  $(document).ready(function () {

      $('.box-section .counter').each(function () {
          $(this).prop('Counter', 0).animate({
              Counter: $(this).text()
          }, {
              duration: 4000,
              easing: 'swing',
              step: function (now) {
                  $(this).text(Math.ceil(now));
              }
          });
      });
      
      });