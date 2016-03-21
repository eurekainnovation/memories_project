
    
$(document).ready( function() {
    
    
		$(function() {
        	$(".card").flip({
           		trigger: 'click'
        	});
			document.getElementById('post_btn').focus();
        $(".noflips").click(function(event) {
    		event.stopPropagation();
			});
    	});


});










