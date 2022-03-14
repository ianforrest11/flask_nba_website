function deleteNote(noteId) {
    fetch('/delete-note', {
        method:'POST',
        body:JSON.stringify({ noteId:noteId })
    }).then((_res) => {
        window.location.href = '/';
    });
}


$(function() {
    $("#toggle").click(function() {
        if ($(this).is(":checked")) {
        $("#stats1").show();
        $("#stats2").hide();
        } else {
        $("#stats1").hide();
        $("#stats2").show();
        }
    });
    });

$(function() {
    $("#myswitch").click(function() {
        if ($(this).is(":checked")) {
        $("#totals").show();
        $("#pg").hide();
        } else {
        $("#totals").hide();
        $("#pg").show();
        }
    });
    });