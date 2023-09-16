$(document).ready(function() {
     const csrftoken = getCookie('csrftoken');

    // Function to get the value of a cookie by name
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
     $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(".upvote-button").click(function() {
        const tipId = $(this).data("tip-id");
        $.post(`/tip/${tipId}/upvote/`, function(data) {
            // Update the upvote and downvote counts on the page
            console.log(data);
            $(`.upvote-count-${tipId}`).text(data.upvotes);
            $(`.downvote-count-${tipId}`).text(data.downvotes);
        });
    });

    $(".downvote-button").click(function() {
        const tipId = $(this).data("tip-id");
        $.post(`/tip/${tipId}/downvote/`, function(data) {
            // Update the upvote and downvote counts on the page
            $(`.upvote-count-${tipId}`).text(data.upvotes);
            $(`.downvote-count-${tipId}`).text(data.downvotes);
        });
    });
    $(".delete-button").click(function() {
        const tipId = $(this).data("tip-id");
        $.post(`/tip/${tipId}/delete/`, function(data) {
            // Update the upvote and downvote counts on the page
            $(`.tip-${tipId}`).remove();
        });
    });
});
