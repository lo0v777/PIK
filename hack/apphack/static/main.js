document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll('.button');
    buttons.forEach(function(button) {
      button.addEventListener('click', function() {
        var link = button.querySelector('a');
        var href = link.getAttribute('href');
        window.location.href = href;
      });
    });
  });
  