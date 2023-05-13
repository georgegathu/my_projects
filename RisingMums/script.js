// This code will make the website responsive, so that it will automatically adjust to fit the size of the screen it is being viewed on.

window.addEventListener('resize', function() {
  var width = window.innerWidth;
  if (width < 768) {
    body {
      font-size: 14px;
    }
  } else {
    body {
      font-size: 16px;
    }
  }
});

// This code will add a smooth scroll effect to the website.

$(document).ready(function() {
  $('a[href^="#"]').on('click', function(e) {
    e.preventDefault();
    var target = $(this).attr('href');
    $('html, body').animate({
      scrollTop: $(target).offset().top - 50
    }, 500);
  });
});
