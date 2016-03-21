$(function() {

    $("#file_upload_form").submit(function() {
        var error_photo = false;                          

        if ($('#id_photo').get(0).files.length === 0) {
            $("#id_photoe").html("Select a photo to upload");
            $("#id_photoe").show();
            error_photo = true;
        }

        if(error_photo == false ) {
            return true;
        } else {
            return false;   
        }

    });

});