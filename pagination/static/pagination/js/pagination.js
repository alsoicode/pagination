jQuery(function($){

    // Handler for items per page form
    $('.items-per-page, .paginator').change(function(e){
        $(e.target).parents('form:first').submit();
    });

});