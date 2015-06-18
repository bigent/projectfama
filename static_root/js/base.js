/**
 * Created by bigent on 11.6.2015.
 */

$(document).ready( function(){
    var width = $('#bar').width() - 110.5;
    $('#bar .menus').css('width', width/2);
    $('#menus .menus .text').css('width', width/2);
    $('#menus .menus .text').css('min-width', width/2);
});


$('#bar #user-tab').mouseover( function(){
    $('#user-tab #others').css("display", "block");
});


$('#bar #user-tab').mouseout( function(){
    $('#user-tab #others').css("display", "none");
});

$(window).resize( function(){
    var width = $('#bar').width() - 110.5;
    $('#bar .menus').css('width', width/2);
    $('#menus .menus .text').css('width', width/2);
    $('#menus .menus .text').css('min-width', width/2);
});
