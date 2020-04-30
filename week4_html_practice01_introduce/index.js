$(document).ready(function(){
  $("#guntlet").click(function(){
    $("#ironman").fadeToggle();
    $("#hulk").fadeToggle("slow");
    $("#groot").fadeToggle(3000);
  });
});