const commentContainer = $('#comments_container');

const addComment = () => {
    $.LoadingOverlay("show");
    resetAlerts();

    const comment = $('#comment').val();
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        type: 'POST',
        url: URLS.add_comment,
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrfToken
        },
        data: JSON.stringify({
            comment: comment
        }),
        success: function({view, is_toxic, message}) {
            if(is_toxic) {
                showAlert(message, 'warning');
                $('#comment').val('');
                $.LoadingOverlay("hide");
                return;
            }

            showAlert(message, 'success');
            $('#comment').val('');
            commentContainer.append(view);

            $.LoadingOverlay("hide");
        },
        error: function(xhr, status, error) {
            alert('Error');
            console.error('Error adding comment:', error);
        
            $.LoadingOverlay("hide");
        }
    });
};

$(document).ready(function() {
    $('button').click(addComment);
});