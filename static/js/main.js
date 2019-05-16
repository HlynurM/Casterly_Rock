$(document).ready(function () {
    $(function () {
        $('[data-toggle="popover"]').popover()
    })
})

// $(document).ready(function () {
//     $("[data-toggle=popover]").popover({
//         html: true,
//         content: function () {
//             var content = $(this).attr("data-popover-content");
//             return $(content).children(".popover-body").html();
//         },
//         title: function () {
//             var title = $(this).attr("data-popover-content");
//             return $(title).children(".popover-heading").html();
//         }
//     });
// });

// $(document).ready(function () {
//     $("[data-toggle=popover]").each(function (i, obj) {
//         $(this).popover({
//             html: true,
//             content: function () {
//                 var id = $(this).attr('id')
//                 return $('#popover-content-' + id).html();
//             }
//         });
//     });
// });
// $(document).ready(function () {
//     var popupElement = '<div class="btn-group btn-toggle"><button class="btn btn-sm btn-info">On</button><button class="btn btn-sm btn-primary active">Off</button></div>';
//
//     $('#popbutton').popover({
//         animation: true,
//         content: popupElement,
//         html: true
//     });
//
//
//     $('body').on('click', '.btn-toggle', function () {
//         $(this).find('.btn').toggleClass('active');
//
//         if ($(this).find('.btn-primary').length > 0) {
//             $(this).find('.btn').toggleClass('btn-primary');
//         }
//         if ($(this).find('.btn-danger').length > 0) {
//             $(this).find('.btn').toggleClass('btn-danger');
//         }
//         if ($(this).find('.btn-success').length > 0) {
//             $(this).find('.btn').toggleClass('btn-success');
//         }
//         if ($(this).find('.btn-info').length > 0) {
//             $(this).find('.btn').toggleClass('btn-info');
//         }
//
//         $(this).find('.btn').toggleClass('btn-default');
//     });
// });