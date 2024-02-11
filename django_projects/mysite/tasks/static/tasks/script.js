// tasks/script.js
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.delete-task').forEach(function (button) {
        button.addEventListener('click', function () {
            var taskId = button.getAttribute('data-task-id');
            fetch('/delete/' + taskId + '/', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                button.closest('li').remove();
            })
            .catch(error => console.error('Error:', error));
        });
    });

    function getCookie(name) {
        var value = "; " + document.cookie;
        var parts = value.split("; " + name + "=");
        if (parts.length == 2) return parts.pop().split(";").shift();
    }
});
