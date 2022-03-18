function deleteNote(noteId) {
    fetch('/delete-note', {
        method:'POST',
        body:JSON.stringify({ noteId:noteId })
    }).then((_res) => {
        window.location.href = '/';
    });
}

//test function
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

//function to hide and show tables based on which view is selected
// $(function() {
$("#pg").hide();
$("#myswitch").on('change', function() {
    $('#pg').show();
    $('#totals').hide();
    if ($(this).is(":checked")) {
    $("#pg").show();
    $("#totals").hide();
    } else {
    $("#pg").hide();
    $("#totals").show();
    }
});
// });


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
            txtValue_full = txtValue + txtValue_last 
            if (txtValue_full.toUpperCase().indexOf(filter) > -1) {
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
            txtValue_full = txtValue + txtValue_last 
            if (txtValue_full.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }       
    }
    }

$('input[type=checkbox]').on('change', function(){
    
    // constants
    var id = $(this).prop('id');
    // make sure function does not affect totals/per-game switch
    if (id.toLowerCase().indexOf("myswitch") === -1) {
        alert('change')
        var elem = $(this);

        // if avg box gets checked
        var pattern1 = /add-player-avg-/;
        var suffix1 = this.id.match(/\d+/);

        //returns true or false...
        var exists1 = pattern1.test(id);
        if ((exists1) && (elem.is(":checked"))) {
            alert('yasss')
            $('#add-player-total-' + suffix1).prop('checked', true)
        //true statement, do whatever
        } else if ((exists1) && (elem.not(":checked"))) {
            alert('nahhh')
            $('#add-player-total-' + suffix1).prop('checked', false)
        }
    }

    // if totals box gets checked
    var pattern2 = /add-player-total-/;
    var suffix2 = this.id.match(/\d+/);

    //returns true or false...
    var exists2 = pattern2.test(id);
    if ((exists2)  && (elem.is(":checked"))) {
        alert('yasss')
        $('#add-player-avg-' + suffix2).prop('checked', true)
    //true statement, do whatever
    } else if ((exists2) && (elem.not(":checked"))) {
        alert('nahhh')
        $('#add-player-avg-' + suffix2).prop('checked', false)
    }
});