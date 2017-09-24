
$SCRIPT_ROOT = ''

function updateStatus() {
    $.getJSON($SCRIPT_ROOT + '/lock_status', {}, function(data) {
        lockImage = document.getElementById('door-lock-img');
        unlockImage = document.getElementById('door-unlock-img');

        if (data.locked) {
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
        $.get($SCRIPT_ROOT + '/lock?lock=false', function(data) {
            updateStatus();
        });
    });
});

$(function() {
    $('#door-unlock-img').on("click", function(data) {
        $.get($SCRIPT_ROOT + '/lock?lock=true', function(data) {
            updateStatus();
        });
    });
});

updateStatus();