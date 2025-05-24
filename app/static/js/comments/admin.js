const denyComment = (commentId) => {
    $.LoadingOverlay("show");

    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        type: 'POST',
        url: URLS.deny_comment,
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrfToken
        },
        data: JSON.stringify({
            id: commentId
        }),
        success: function({message}) {
            $(`#comment_${commentId}`).remove();
            showAlert(message, 'success');

            $.LoadingOverlay("hide");
        },
        error: function(xhr, status, error) {
            alert('Error');
            console.error('Error deny comment:', error);
            
            $.LoadingOverlay("hide");
        }
    });
};

const approveComment = (commentId) => {
    $.LoadingOverlay("show");

    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        type: 'POST',
        url: URLS.approve_comment,
        dataType: 'json',
        headers: {
            'X-CSRFToken': csrfToken
        },
        data: JSON.stringify({
            id: commentId
        }),
        success: function({message}) {
            $(`#comment_${commentId}`).remove();
            showAlert(message, 'success');

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
    $(document).on('click', 'button.accept', function() {
        const commentId = $(this).data('id');
        approveComment(commentId);
    });

    $(document).on('click', 'button.deny', function() {
        const commentId = $(this).data('id');
        denyComment(commentId);
    });
});