$(document).ready(function () {
    $('#search-button').on('click', function(e) {
        //Event listener
        // console.log("Search pressed!")
        e.preventDefault();
        var searchText = $('#search-bar').val();
        // console.log("This is the search terms: " + searchText)
        $.ajax( {
            url: '/estates?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                // console.log("im inside ajax: " + resp)
                var newHtml = resp.data.map(d => {
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
                });
                // console.log("This is the html string: " + newHtml)
                $('.estates').html(newHtml.join(''));
                $('#search-bar').val(  '');
            },
            error: function(xhr, status, error) {
                console.log("hot damn!")
                console.error(error);
            }
        })
    });
});

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