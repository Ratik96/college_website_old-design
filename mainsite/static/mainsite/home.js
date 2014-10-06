// function slideSwitch() {
//     var $active = $('#slideshow IMG.active');
//     if ($active.length == 0) $active = $('#slideshow IMG:last');

//     var $next =  $active.next().length ? $active.next()
//         : $('#slideshow IMG:first');

//     $active.addClass('last-active');
        
//     $next.css({opacity: 0.0})
//         .addClass('active')
//         .animate({opacity: 1.0}, 1000, function() {
//             $active.removeClass('active last-active');
//         });
// }

// $(function() {
//     setInterval( "slideSwitch()", 5000 );
// });

$(document).ready(function(){
    $('#myslider').juicyslider({
        mode: "cover",
        width: '100%',
        height: '100%',
        mask: "raster",
        bgcolor: "#000",
        autoplay: 20000,                             
        shuffle: true,                             
        show: {effect: 'puff', duration: 2000},     
        hide: {effect: 'puff', duration: 2000},
    });
});


