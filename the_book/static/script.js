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

function addToShelf(event, bookId) {

    event.preventDefault();
    const msg = document.createElement("div");
    const pageDiv = document.getElementById('content-page');
    const secPart = document.getElementById('sec-par');
    msg.setAttribute("id", "alert-message")

    fetch("/book_detail/" + bookId + "/add_to_shelf", {
        method: "POST",
    })
        .then(
            function (response) {
                if (response.status === 201) {
                    msg.setAttribute("class", "w-75 mx-auto mt-3 alert alert-success");
                    msg.textContent = "The book is successfully added to your shelf!";
                    pageDiv.insertBefore(msg, secPart);
                    setTimeout(() => { pageDiv.removeChild(msg) }, 3000);
                }
                //show the fail msg to the view
                else if (response.status === 409) {
                    // let alert = document.getElementById("alert-message")
                    // if (pageDiv.contains(alert)) {
                    //     pageDiv.removeChild(alert)
                    // }
                    msg.setAttribute("class", "w-75 mx-auto mt-3 alert alert-info");
                    msg.textContent = "The book is already in your shelf.";
                    pageDiv.insertBefore(msg, secPart);
                    setTimeout(() => { pageDiv.removeChild(msg) }, 3000);
                }
                // redirect to login page if user is not logged in
                else if (response.redirected) {
                    window.location.href = response.url
                }
                else {
                    console.log("Looks like there was a problem.")
                }
            }
        )
        .catch(function (err) {
            console.log("Fetch error: ", err)
        })
}

function addRating(event, bookId) {

    event.preventDefault();
    const formData = new FormData(document.getElementById("rate"));
    const msg = document.createElement("div");
    const pageDiv = document.getElementById('content-page');
    const secPart = document.getElementById('sec-par');
    msg.setAttribute("id", "alert-message")

    fetch("/book_detail/" + bookId + "/add_rating", {
        method: "POST",
        body: formData
    })
        .then(
            function (response) {
                if (response.status === 201) {
                    msg.setAttribute("class", "w-75 mx-auto mt-3 alert alert-success");
                    msg.textContent = "Your ratings have been added!";
                    pageDiv.insertBefore(msg, secPart);
                    setTimeout(() => { pageDiv.removeChild(msg) }, 3000);
                }
                //show the fail msg to the view
                else if (response.status === 409) {
                    let alert = document.getElementById("alert-message")
                    if (pageDiv.contains(alert)) {
                        pageDiv.removeChild(alert)
                    }
                    msg.setAttribute("class", "w-75 mx-auto mt-3 alert alert-info");
                    msg.textContent = "Your ratings have been updated.";
                    pageDiv.insertBefore(msg, secPart)
                    setTimeout(() => { pageDiv.removeChild(msg) }, 3000);
                }
                // redirect to login page if user is not logged in
                else if (response.redirected) {
                    window.location.href = response.url
                } else {
                    console.log("Looks like there was a problem.")
                }
            }
        )
        .catch(function (err) {
            console.log("Fetch error: ", err)
        })
}