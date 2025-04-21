const resetAlerts = () => {
    $('.alerts .alert').each(function(index, el) {
        $(el).addClass('d-none');
        $(el).text('');
    });
};

const showAlert = (message, type) => {
    let alert = null;

    switch (type) {
        case 'success':
            alert = $('#success-comment');

            break;
            
        case 'warning':
            alert = $('#warning-comment');
            break;

        default:
            throw new Error('Invalid alert type');
    }

    alert.removeClass('d-none');
    alert.text(message);
};