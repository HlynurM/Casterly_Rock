function html(d) {
    return `<div class="col-md-4">
                    <div class="card mb-4 box-shadow well">
                        <a href="/estates/${d.id}">
                            <img class="estate-img" src="${d.firstImage}" alt="${d.name}"/>
                            <div class="card-body">
                                <h4 class="card-address">${d.name}</h4>
                                <h3 class="card-price">${d.price}</h3>
                                <p class="card-short-description">${d.description}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div class="btn-group">
                                        <a href="/estates/${d.id}" class="btn btn-sm btn-outline-danger">View</a>    
                                    </div>
                                    <small class="text-muted">9 mins</small>
                                </div>
                            </div>
                        </a>
                    </div>
            </div>`
};

function check_priceDropDown() {
    if ($('#priceDropdown').val() === "") {
        return [0, 99999999999999999]
    } else if ($('#priceDropdown').val() === "1") {
        return [0, 200000000]
    } else if ($('#priceDropdown').val() === "2") {
        return [200000000, 400000000]
    } else if ($('#priceDropdown').val() === "3") {
        return [400000000, 600000000]
    } else if ($('#priceDropdown').val() === "4") {
        return [600000000, 800000000]
    } else if ($('#priceDropdown').val() === "5") {
        return [800000000, 99999999999999999]
    }
};

function check_sizeDropDown() {
    if ($('#sizeDropdown').val() === "") {
        return 0
    } else if ($('#sizeDropdown').val() === "1") {
        return [0, 200]
    } else if ($('#sizeDropdown').val() === "2") {
        return [200, 400]
    } else if ($('#sizeDropdown').val() === "3") {
        return [400, 600]
    } else if ($('#sizeDropdown').val() === "4") {
        return [600, 800]
    } else if ($('#sizeDropdown').val() === "5") {
        return [800, 99999999999999999]
    }
};

function check_onSaleCheckbox() {

    if ($('#on_saleCheck').prop('checked')) {
        return "ok"
    } else {
        return "nei"
    }
};

function generateFilter() {

    var filter = {};

    if ($('#on_saleCheck').prop('checked')) {
        filter["on_sale"] = true
    } else {
        filter["on_sale"] = false
    }

    filter["priceRange"] = check_priceDropDown()


    return filter

    };


$(document).ready(function () {
    $('#search-button').on('click', function (e) {

        e.preventDefault();
        var searchText = $('#search-bar').val();
        var priceRange = check_priceDropDown();
        var sizeRange = check_sizeDropDown();


        $.ajax({
            url: '/estates?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {

                    filter = generateFilter()


                    if (filter["priceRange"][0] < d.price && d.price < filter['priceRange'][1]) {
                        if (filter['on_sale'] === d.on_sale) {
                            console.log(d)
                            return html(d)
                        }




                     }

                });

                var notFound = `<h4> Engar eignir fundust. Reyndu aftur!</h4>`

                if (newHtml == "" || newHtml.join('') == "") {

                    $('.estates').html(notFound);
                    $('#search-bar').val('');

                } else {

                    $('.estates').html(newHtml.join(''));
                    $('#search-bar').val('');
                }




                // if (newHtml == ""){
                //     console.log('vesen 1')
                //     $('.castles').html(notFound);
                //     $('#search-box').val('');
                // } else {
                //     console.log('vesen 2')
                //
                //     $('.castles').html(newHtml.join(''));
                //     $('#search-box').val('');
                //
                //
                // };


            },


            error: function (xhr, status, error) {
                console.log("hot damn!")
                console.error(error);
            }
        })
    });
});

// $(document).ready(function () {
//     $('#search-button').on('click', function (e) {
//
//         e.preventDefault();
//         var searchText = $('#search-bar').val();
//         var priceRange = check_priceDropDown();
//         var sizeRange = check_sizeDropDown();
//         var if_onSale = check_onSaleCheckbox();
//
//         console.log(generateFilter())
//         console.log('yo!')
//         console.log(searchText + ' asses')
//             $.ajax({
//             url: '/estates?search_filter=' + searchText,
//             type: 'GET',
//             success: function (resp) {
//
//                 console.log('Here we go:')
//                 var filter = generateFilter()
//
//                 var newHtml = resp.data.map(d => {
//
//                     console.log(d.name, d.on_sale, d.price)
//
//                     if (filter['priceRange'][0] < d.price && d.price < filter['priceRange'][1]) {
//
//                         if (d.on_sale === filter['on_sale']) {
//                             return html(d)
//                         };
//
//                     };
//
//
//                 });
//
//                 var notFound = `<h4> Engar eignir fundust. Reyndu aftur!</h4>`
//
//                 if (newHtml == "" || newHtml.join('') == "") {
//
//                     $('.estates').html(notFound);
//                     $('#search-bar').val('');
//
//                 } else {
//
//                     $('.estates').html(newHtml.join(''));
//                     $('#search-bar').val('');
//                 }
//
//
//
//
//                 // if (newHtml == ""){
//                 //     console.log('vesen 1')
//                 //     $('.castles').html(notFound);
//                 //     $('#search-box').val('');
//                 // } else {
//                 //     console.log('vesen 2')
//                 //
//                 //     $('.castles').html(newHtml.join(''));
//                 //     $('#search-box').val('');
//                 //
//                 //
//                 // };
//
//
//             },
//
//
//             error: function (xhr, status, error) {
//                 console.log("hot damn!")
//                 console.error(error);
//             }
//         })
//     });
// });



// $(document).ready(function(){
//             $("#txtSearch").autocomplete({
//                 source: "/ajax_calls/search/",
//                 minLength: 2,
//                 open: function(){
//                     setTimeout(function () {
//                         $('.ui-autocomplete').css('z-index', 99);
//                     }, 0);
//                 }
//               });
//
//         });