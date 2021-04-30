jQuery(function () {

    var minimized_elements = $('p.description');

    minimized_elements.each(function () {
        var t = $(this).text();
        if (t.length < 300) return;

        $(this).html(
            t.slice(0, 300) + '<span>... </span><a href="#" class="more">More</a>' +
            '<span style="display:none;">' + t.slice(100, t.length) + ' <a href="#" class="less">Less</a></span>'
        );

    });

    $('a.more', minimized_elements).click(function (event) {
        event.preventDefault();
        $(this).hide().prev().hide();
        $(this).next().show();
    });

    $('a.less', minimized_elements).click(function (event) {
        event.preventDefault();
        $(this).parent().hide().prev().show().prev().show();
    });

});

function addToShelf(bookId) {
    // TODO: login required

    //TODO: get book_id 

    //TODO: fetch a route use post method, body with book_id
    fetch("/api/shelf", {
        method: "POST",
        body: bookId
    })
        //TODO: fetch .then  get the response
        .then(
            function (response) {
                if (response != 201) {
                    console.log(
                        "Looks like there was a problem. Status Code: " + response.status
                    );
                }
                //TODO: show the success msg to the view
                const add = document.getElementById("add-to-shelf")
                const msg = document.createElement("div")
                msg.setAttribute("class", "alert")
                msg.textContent("The book is successfully added to your shelf!")
            }
        )
        // TODO: fetch .catch
        .catch(function (err) {
            console.log("Fetch error: ", err)
        })
}
