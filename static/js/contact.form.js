
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(function() {

    $("#submit-contact").click(function(){

        var email = $("#InputEmail").val()
        var name  = $("#InputName").val()
        var message = $("#InputText").val()
        var csrftoken = getCookie('csrftoken')
        var url = '/landing/contact/' //window.location.href

        var data_obj = {
          'email' : email,
          'name' : name,
          'message' : message,
          'csrftoken' : csrftoken
        }

        cosole.log(data_obj)
        alert(JSON.stringify(data_obj))


        $.ajax({

         url : url,
         type: "POST",
         data : data_obj,
         dataType : "json",
         success: function(data ){
              alert(JSON.stringify(data))
            }
        });

    //alert(JSON.stringify(data_obj))


    });

});
