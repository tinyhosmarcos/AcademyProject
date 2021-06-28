$(document).ready(function(){
  $('.tooltipped').tooltip();
  $('.sidenav').sidenav();
  $('.parallax').parallax();
  $('.modal').modal();
  $('.tabs').tabs();
  $('ul.tabs').tabs();
  $('.collapsible').collapsible();
  $('.carousel.carousel-slider').carousel({
      fullWidth: true,
      indicators: true,
      duration: 400
    });
  
  $('.tap-target').tapTarget();
  $(".dropdown-trigger").dropdown({
    coverTrigger: false,
    hover: true,
    constrainWidth:false
  });
  $('#formulariopago').on('submit', function(e){
    e.preventDefault();
    $('#modal1').modal('close'); 
    $('#modal2').modal('open'); 
  });
  inicial();
  function inicial(){
    setTimeout(autoplay, 2500);
  }
  function autoplay() {
    $('.carousel.carousel-slider').carousel('next');
    setTimeout(autoplay, 4500);
}

});