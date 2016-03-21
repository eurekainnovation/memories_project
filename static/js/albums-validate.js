$(function() {

    var error_title = false;

    $("#id_title").focusout(function(){
        check_username();
    });

    function check_username() {
    
        var username_length = $("#id_title").val().length;
        
        if(username_length ==0) {
            $("#id_titlee").html("Enter a name for the album title");
            $("#id_titlee").show();
            error_title = true;
        } else {
            $("#id_titlee").hide();
        }
    
    }

    $("#new_album_form").submit(function() {
        var error_photo = false;                          
        error_title = false;                      
        check_username();

        if ($('#id_cover').get(0).files.length === 0) {
            $("#id_covere").html("Select a photo to upload");
            $("#id_covere").show();
            error_photo = true;
        }

        if(error_title == false && error_photo == false ) {
            return true;
        } else {
            return false;   
        }

    });

});