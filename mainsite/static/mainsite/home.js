function slideSwitch() {
    var $active = $('#slideshow IMG.active');

    if ( $active.length == 0 ) $active = $('#slideshow IMG:last');

    var $next =  $active.next().length ? $active.next()
        : $('#slideshow IMG:first');

    $active.addClass('last-active');
        
    $next.css({opacity: 0.0})
        .addClass('active')
        .animate({opacity: 1.0}, 1000, function() {
            $active.removeClass('active last-active');
        });
}

$(function() {
    setInterval( "slideSwitch()", 5000 );
});

//..............................
$(document).ready(function()
{

	$(".menu").click(function()
	{
		var X=$(this).attr('id');
		
		if(X==1)
		{
		$(".submenu").slideUp();
		$(this).attr('id', '0');
		}
		else
		{

		$(".submenu").slideDown();
		$(this).attr('id', '1');
		}
		
		});

	
});
