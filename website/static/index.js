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

function validate(){
    var remember = document.getElementById(this.id);
    if (remember.checked){
        alert("checked") ;
    }else{
        alert("You didn't check it! Let me check it for you.")
    }
}

function Validate() {
    var checked = 0;

    //Reference the Table.
    var tblPlayers1 = document.getElementById("playertable");

    //Reference all the CheckBoxes in Table.
    var chks = tblPlayers1.getElementsByTagName("INPUT");

    //Loop and count the number of checked CheckBoxes.
    for (var i = 0; i < chks.length; i++) {
        if (chks[i].checked) {
            checked++;
        }
    }

    if (checked > 0) {
        alert(checked + " CheckBoxe(s) are checked.");
        return true;
    } else {
        alert("Please select CheckBoxe(s).");
        return false;
    }
};

// $("input[type=checkbox]").each(function() {
//     var elem = $(this);
//     if (elem.is(":checked")) {
//         alert("checked")
//        // Item is checked
//     }
// })

$('input[type=checkbox').on('change', function(){
    alert('change')
    // constants
    var id = $(this).prop('id');
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