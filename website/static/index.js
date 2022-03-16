function deleteNote(noteId) {
    fetch('/delete-note', {
        method:'POST',
        body:JSON.stringify({ noteId:noteId })
    }).then((_res) => {
        window.location.href = '/';
    });
}


$(function() {
    $("#stats2").hide();
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
    $("#totals").hide();
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


function searchPlayers() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("query");
    filter = input.value.toUpperCase();
    table = document.getElementById("playerTable");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
        td_first_name = tr[i].getElementsByTagName("td")[0];
        td_last_name = tr[i].getElementsByTagName("td")[1];
        if (td_first_name || td_last_name) {
        txtValue = td_first_name.textContent || td_first_name.innerText;
        txtValue_last = td_last_name.textContent || td_last_name.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1 || txtValue_last.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
        }       
    }
    table = document.getElementById("playertable2")
    tr = table.getElementsByTagName("tr"); 
    for (i = 0; i < tr.length; i++) {
        td_first_name = tr[i].getElementsByTagName("td")[0];
        td_last_name = tr[i].getElementsByTagName("td")[1];
        if (td_first_name || td_last_name) {
        txtValue = td_first_name.textContent || td_first_name.innerText;
        txtValue_last = td_last_name.textContent || td_last_name.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1 || txtValue_last.toUpperCase().indexOf(filter) > -1) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
        }       
    }
    }

const cb = document.querySelector('#add-player-average-1');
console.log(cb.checked);