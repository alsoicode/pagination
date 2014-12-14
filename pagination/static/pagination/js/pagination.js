!function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        define('jquery', factory);
    } else {
        factory(root.jQuery);
    }
}(this, function($) {
    $(document).ready(function() {
        // Handler for items per page form
        $('.items-per-page, .paginator').change(function(e){
            $(e.target).parents('form:first').submit();
        });
    });
});