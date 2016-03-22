$(document).ready(function() {

$('#save-add-user').click(function(){
	$('#addModal').modal('toggle');
});

$('#collaborator').keyup(function(){

	var query;
	query = $(this).val();
	$.get('/suggest_users/', {suggestion:query}, function(data){

	var availableTags = [
      "ActionScript",
      "AppleScript",
      "Asp",
      "Scheme"
    ];

	$('#collaborator').autocomplete({delay: 0, source:data});
	//$('#testing').html(availableTags);



});

});
});


function postmsg(form,val,photo,url) {

//alert('something!! :D');
if (!form.comment.value==""){
document.getElementById(val+'new_msg').innerHTML +='<div style="backface-visibility: hidden;" class="row thread"> <div style="backface-visibility: hidden;" class="col-xs-2"><img style="backface-visibility: hidden;" class="img-circle center-block" src='+ photo + ' alt="pic" height="50" width="50"></div><div style="backface-visibility: hidden;" class="col-xs-10 id=" message"=""><p  style="backface-visibility: hidden;">' + form.comment.value + '</p></div></div>';
form.submit();
form.comment.value = ""
}



};