$('#write-fama').click( function() {
    if ($('#add-famas form').css('display') == "block"){
        $('#add-famas form').css('display', 'none');
    } else if ($('#add-famas form').css('display') == "none") {
        $('#add-famas form').css('display', 'block');
    }
});

//if results's box is empty, press the text
if ($('#results').text() == false){
            $('#results').append('<span id="no-results">No found results</span>');
        }