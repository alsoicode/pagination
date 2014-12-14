!function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        define(['jquery'], factory);
    } else {
        factory(root.jQuery);
    }
}(this, function($) {
    'use strict';

    $(document).ready(function() {
        // Handler for items per page form
        $('.items-per-page').change(function(e){
            $(e.target).parents('form:first').submit();
        });

        // Handler for Page x of y form
        $('.paginator select').change(function(e) {
            var element = $(this),
                form = element.parents('form:first'),
                action = form.attr('action'),
                concatenator = action.indexOf('?') == -1 ? '?' : '&',
                url = action + concatenator + 'page=' + element.val();
            window.top.location = url;
        })
    });
});