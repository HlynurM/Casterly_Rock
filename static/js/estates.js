function check_priceDropDown() {
    if ($('#priceDropdown').val() === "") {
        return [0, 99999999999999999]
    } else if ($('#priceDropdown').val() === "1") {
        return [0, 200000]
    } else if ($('#priceDropdown').val() === "2") {
        return [200000, 400000]
    } else if ($('#priceDropdown').val() === "3") {
        return [400000, 600000]
    } else if ($('#priceDropdown').val() === "4") {
        return [600000, 800000]
    } else if ($('#priceDropdown').val() === "5") {
        return [800000, 99999999999999999]
    }
};

function check_roomsDropDown() {
    if ($('#roomsDropdown').val() === "") {
        return [0, 9999999999999999999999]
    } else if ($('#roomsDropdown').val() === "1") {
        return [0, 4]
    } else if ($('#roomsDropdown').val() === "2") {
        return [4, 8]
    } else if ($('#roomsDropdown').val() === "3") {
        return [8, 12]
    } else if ($('#roomsDropdown').val() === "4") {
        return [12, 16]
    } else if ($('#roomsDropdown').val() === "5") {
        return [16, 99999999999999999]
    }
};


function generateFilter() {

    var filter = {};

    if ($('#on_saleCheck').prop('checked')) {
        filter["on_sale"] = true
    } else {
        filter["on_sale"] = false
    }
    if ($('#moatCheck').prop('checked')) {
        filter["moat"] = true
    } else {
        filter["moat"] = false
    }

    filter["priceRange"] = check_priceDropDown()
    filter["roomsRange"] = check_roomsDropDown()

    return filter

};

$(document).ready(function () {
    $('#search-button').on('click', function (e) {
        //Event listener
        // console.log("Search pressed!")
        e.preventDefault();
        var searchText = $('#search-bar').val();
        // console.log("This is the search terms: " + searchText)

        //ÞARF AÐ SLEPPA ÞESSU ÚT AF SÍUNNI

        // if (searchText == "") {
        //         //      console.log("search is empty. Do nothing.");
        //         // } else {
        $.ajax({
            url: '/estates?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHtml = resp.data.map(d => {

                    filter = generateFilter()
                    console.log(d.name, d.price, d.rooms)
                    console.log(filter["roomsRange"])

                    if (filter["priceRange"][0] < d.price && d.price < filter['priceRange'][1]) {
                        if (filter["roomsRange"][0] < d.rooms && d.rooms < filter['roomsRange'][1]) {
                            if (filter['on_sale'] === d.on_sale) {
                                return `<div class="col-md-4">
                                <div class="card estate_box shadow-sm">
                                    <a href="/estates/${d.id}">
                                        <div class="thumbnail">
                                            <img class="thumbnail" src="${d.firstImage}" alt="${d.name}"
                                                 alt="{{ estate.name }}"/>
                                        </div>
                                        <div class="card-body">
                                            <h4 class="card-address">${d.name}</h4>
                                            <h3 class="card-price">${d.price} <i class="fas fa-coins gold" color="#FB8F2B"></i></h3>
                                            <p class="card-short-description">${d.description}</p>
                                            <div class="text-right">
                                                <small class="text-muted text-right"><i class="far fa-star gold"></i></small>
                                            </div>
                                        </div>
                                    </a>
                                </div>
                            </div>`
                            }
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

            },
            error: function (xhr, status, error) {
                console.log("hot damn!")
                console.error(error);
            }
        })
        //}
    });
});




