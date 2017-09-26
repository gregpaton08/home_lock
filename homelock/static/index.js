
$SCRIPT_ROOT = ''

function updateStatus() {
    $.getJSON($SCRIPT_ROOT + '/api/v1/lock_status', {}, function(data) {
        lockImage = document.getElementById('door-lock-img');
        unlockImage = document.getElementById('door-unlock-img');

        if (data.status) {
            unlockImage.style.display = 'none';
            lockImage.style.display = 'block';
        } else {
            lockImage.style.display = 'none';
            unlockImage.style.display = 'block';
        }
    });
}

$(function() {
    $('#door-lock-img').on("click", function(data) {
        $.ajax({
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            url: '/api/v1/lock_status',
            method: 'PUT',
            data: JSON.stringify({ 'status' : false }),
            success: function() {
                updateStatus();
            }
        })
    });
});

$(function() {
    $('#door-unlock-img').on("click", function(data) {
        $.ajax({
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            url: '/api/v1/lock_status',
            method: 'PUT',
            data: JSON.stringify({ 'status' : true }),
            success: function() {
                updateStatus();
            }
        })
    });
});

updateStatus();