$(document).ready(function () {
    $('#search-button').on(types: 'click', selector: function(e) {
        console.log("Search pressed!")
        e.preventDefault();
        var searchText = $('#search-bar').val();
        $.ajax(url: {
            url: '/estates/?search_filter=' + searchText,
                type: 'GET',
                success: function(resp) {
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
                    $('.estates').html(newHtml.join(''));
                    $('#search-bar').val( value: '');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});