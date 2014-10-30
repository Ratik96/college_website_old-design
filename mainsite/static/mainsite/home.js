$(document).ready(function(){
  $('#myslider').juicyslider({
    mode: "cover",
    width: '100%',
    height: '100%',
    mask: "none",
    bgcolor: "",
    autoplay: 10000,                        
    shuffle: true,                             
    show: {effect: 'puff', duration: 2000},     
    hide: {effect: 'drop', duration: 2000},
  });
});


