$(document).ready(function() {
    'use strict';
    /*-----------------------------------------------------------------------------------*/
    /*	Show Error message
    /*-----------------------------------------------------------------------------------*/
    $("#error-alert").fadeTo(3500, 500).slideUp(500, function() {
        $("#error-alert").slideUp(500);
    });
});