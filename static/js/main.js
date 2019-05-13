$("[data-toggle=popover]").each(function (i, obj) {

    $(this).popover({
        html: true,
        content: function () {
            var id = $(this).attr('id')
            return $('#popover-content-' + id).html();
        }
    });
});

$(function(){
    // Enables popover
    $("[data-toggle=popover]").popover();
});

$('.popover-dismiss').popover({
  trigger: 'focus'
})

$('.timezone_help').popover({placement: "bottom"});