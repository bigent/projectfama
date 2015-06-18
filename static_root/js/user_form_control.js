/**
 * Created by bigent on 11.6.2015.
 */


$('#id_new_password1').blur(function() {
    var pass1 = $('#id_new_password1')[0];
    var pass2 = $('#id_new_password2')[0];
    var value1 = pass1.value;
    var value2 = pass2.value;

    if(value1 !== ""){
        $('#id_new_password1').removeClass('passed-input');
        $('#id_new_password1').removeClass('error-input');

        if(value1 == ""){
            $('#id_new_password1').removeClass('passed-input');
            $('#id_new_password1').removeClass('error-input');
            $('#id_new_password1').addClass('error-input');
        }else{
            if(value1==value2){
                $('#id_new_password1').removeClass('passed-input');
                $('#id_new_password1').removeClass('error-input');
                $('#id_new_password1').addClass('passed-input');
                $('#id_new_password2').removeClass('passed-input');
                $('#id_new_password2').removeClass('error-input');
                $('#id_new_password2').addClass('passed-input');
            }else{
                $('#id_new_password1').removeClass('passed-input');
                $('#id_new_password1').removeClass('error-input');
                $('#id_new_password1').addClass('error-input');
                $('#id_new_password2').removeClass('passed-input');
                $('#id_new_password2').removeClass('error-input');
                $('#id_new_password2').addClass('error-input');
            }
        }
    }else{
        $('#id_new_password1').removeClass('passed-input');
        $('#id_new_password1').removeClass('error-input');
        $('#id_new_password1').addClass('error-input');
    }
});


$('#id_new_password2').blur(function() {
    var pass1 = $('#id_new_password1')[0];
    var pass2 = $('#id_new_password2')[0];
    var value1 = pass1.value;
    var value2 = pass2.value;

    if(value1 !== ""){
        $('#id_new_password2').removeClass('passed-input');
        $('#id_new_password2').removeClass('error-input');

        if(value1 == ""){
            $('#id_new_password2').removeClass('passed-input');
            $('#id_new_password2').removeClass('error-input');
            $('#id_new_password2').addClass('error-input');
        }else{
            if(value1==value2){
                $('#id_new_password1').removeClass('passed-input');
                $('#id_new_password1').removeClass('error-input');
                $('#id_new_password1').addClass('passed-input');
                $('#id_new_password2').removeClass('passed-input');
                $('#id_new_password2').removeClass('error-input');
                $('#id_new_password2').addClass('passed-input');
            }else{
                $('#id_new_password1').removeClass('passed-input');
                $('#id_new_password1').removeClass('error-input');
                $('#id_new_password1').addClass('error-input');
                $('#id_new_password2').removeClass('passed-input');
                $('#id_new_password2').removeClass('error-input');
                $('#id_new_password2').addClass('error-input');
            }
        }
        }else{
        $('#id_new_password2').removeClass('passed-input');
        $('#id_new_password2').removeClass('error-input');
        $('#id_new_password2').addClass('error-input');
    }
});


$('#id_email').blur(function () {
    var value = $('#id_email')[0].value;

    if(this.value !== ""){
        $('#id_email').removeClass('passed-input');
        $('#id_email').removeClass('error-input');
        var testEmail = /^[A-Z0-9._%+-]+@([A-Z0-9-]+\.)+[A-Z]{2,4}$/i;

        if (!testEmail.test(value)){
            $('#id_email').removeClass('passed-input');
            $('#id_email').removeClass('error-input');
            $('#id_email').addClass('error-input');
        }else{
            $.getJSON("/control-register?email="+value+"&username=", function(data){
                if (data['email'] == "available"){
                    $('#id_email').removeClass('passed-input');
                    $('#id_email').removeClass('error-input');
                    $('#id_email').addClass('error-input');
                }else{
                    $('#id_email').removeClass('passed-input');
                    $('#id_email').removeClass('error-input');
                    $('#id_email').addClass('passed-input');
                }
            });
        }
    }else{
        $('#id_email').removeClass('passed-input');
        $('#id_email').removeClass('error-input');
        $('#id_email').addClass('error-input');
    }
});


if($('#id_password').length == 0){
    $('#id_username').blur(function () {
        if(this.value !== ""){
            $(this).removeClass('passed-input');
            $(this).removeClass('error-input');

            $.getJSON("/control-register?username="+this.value+"&email=", function(data){
                if (data['username'] == "available"){
                    $('#id_username').addClass('error-input');
                }else{
                    $('#id_username').addClass('passed-input');
                }
            });
        }else{
            $(this).addClass('error-input');
        }
    });
}


$('#id_password1').blur(function() {
    var pass1 = $('#id_password1')[0];
    var pass2 = $('#id_password2')[0];
    var value1 = pass1.value;
    var value2 = pass2.value;

    if(value1 !== ""){
        $('#id_password1').removeClass('passed-input');
        $('#id_password1').removeClass('error-input');

        if(value1 == ""){
            $('#id_password1').removeClass('passed-input');
            $('#id_password1').removeClass('error-input');
            $('#id_password1').addClass('error-input');
        }else{
            if(value1==value2){
                $('#id_password1').removeClass('passed-input');
                $('#id_password1').removeClass('error-input');
                $('#id_password1').addClass('passed-input');
                $('#id_password2').removeClass('passed-input');
                $('#id_password2').removeClass('error-input');
                $('#id_password2').addClass('passed-input');
            }else{
                $('#id_password1').removeClass('passed-input');
                $('#id_password1').removeClass('error-input');
                $('#id_password1').addClass('error-input');
                $('#id_password2').removeClass('passed-input');
                $('#id_password2').removeClass('error-input');
                $('#id_password2').addClass('error-input');
            }
        }
    }else{
        $('#id_password1').removeClass('passed-input');
        $('#id_password1').removeClass('error-input');
        $('#id_password1').addClass('error-input');
    }
});

$('#id_password2').blur(function() {
    var pass1 = $('#id_password1')[0];
    var pass2 = $('#id_password2')[0];
    var value1 = pass1.value;
    var value2 = pass2.value;

    if(value1 !== ""){
        $('#id_password2').removeClass('passed-input');
        $('#id_password2').removeClass('error-input');

        if(value1 == ""){
            $('#id_password2').removeClass('passed-input');
            $('#id_password2').removeClass('error-input');
            $('#id_password2').addClass('error-input');
        }else{
            if(value1==value2){
                $('#id_password1').removeClass('passed-input');
                $('#id_password1').removeClass('error-input');
                $('#id_password1').addClass('passed-input');
                $('#id_password2').removeClass('passed-input');
                $('#id_password2').removeClass('error-input');
                $('#id_password2').addClass('passed-input');
            }else{
                $('#id_password1').removeClass('passed-input');
                $('#id_password1').removeClass('error-input');
                $('#id_password1').addClass('error-input');
                $('#id_password2').removeClass('passed-input');
                $('#id_password2').removeClass('error-input');
                $('#id_password2').addClass('error-input');
            }
        }
    }else{
        $('#id_password2').removeClass('passed-input');
        $('#id_password2').removeClass('error-input');
        $('#id_password2').addClass('error-input');
    }
});


$('#form_errors .fa-times').click(function(){
    $('#form_errors').css('display', 'none');
});