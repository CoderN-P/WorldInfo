$(document).ready(function() {
  //cycle through a list of words
  var texts = ["Insert", "Your", "Buzzwords", "Here"];
  var i = 0;
  (function runIt() {
    i++;
    $('.text').fadeOut(3000, function() {
      $('.text').html(texts[i % texts.length]);
      $('.text').fadeIn(500, function() {
        runIt()
      });
    });
  }());
});