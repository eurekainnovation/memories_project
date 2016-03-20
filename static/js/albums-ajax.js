$(document).ready(function() {

$('#collaborator').keyup(function(){

	var query;
	query = $(this).val();
	$.get('/albums/suggest_users/', {suggestion:query}, function(data){	
	
	var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "BASIC",
      "C",
      "C++",
      "Clojure",
      "COBOL",
      "ColdFusion",
      "Erlang",
      "Fortran",
      "Groovy",
      "Haskell",
      "Java",
      "JavaScript",
      "Lisp",
      "Perl",
      "PHP",
      "Python",
      "Ruby",
      "Scala",
      "Scheme"
    ];
	
	$('#collaborator').autocomplete({source:availableTags});	
	$('#testing').html(availableTags);

	
});

});
});


function postmsg(form,val,photo,url) { 

//alert('something!! :D');
if (!form.comment.value==""){
document.getElementById(val+'new_msg').innerHTML +='<div style="backface-visibility: hidden;" class="row" id="thread"> <div style="backface-visibility: hidden;" class="col-xs-2"><img style="backface-visibility: hidden;" class="img-circle center-block" src='+ photo + ' alt="Cinque Terre" height="50" width="50"></div><div style="backface-visibility: hidden;" class="col-xs-10 id=" message"=""><p  style="backface-visibility: hidden;">' + form.comment.value + '</p></div></div>'; 
form.submit();
form.comment.value = ""
}


						 
};