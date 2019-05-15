$(document).ready(function () {
    $('#search-button').on('click', function (e) {
        //Event listener
        // console.log("Search pressed!")
        e.preventDefault();
        var searchText = $('#search-bar').val();
        // console.log("This is the search terms: " + searchText)
        if (searchText == "") {
            console.log("search is empty. Do nothing.");
        } else {
            $.ajax({
                url: '/estates?search_filter=' + searchText,
                type: 'GET',
                success: function (resp) {
                    // console.log("im inside ajax: " + resp)
                    var newHtml = resp.data.map(d => {
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
                    });
                    // console.log("This is the html string: " + newHtml)
                    $('.estates').html(newHtml.join(''));
                    $('#search-bar').val('');
                },
                error: function (xhr, status, error) {
                    console.log("hot damn!")
                    console.error(error);
                }
            })
        }
    });
});