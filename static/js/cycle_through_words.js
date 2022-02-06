
$(document).ready(function() {
  //cycle through a list of words
  $.ajax({
    url: "/getFact",
    dataType: "json",
    success: function cycle(res){
      var words = res;
      var i = 0;
      var interval = setInterval(function(){
        $("#cycle").fadeOut(function(){
          $(this).text(words[i]).fadeIn();
        });
        i++;
        if(i >= words.length){
          i = 0;
        }
      }, 5000);
    }
});
});