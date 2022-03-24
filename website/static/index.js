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

var values = new Array();
$('input[type=checkbox]').on('change', function(){
    // constants
    var id = $(this).prop('id');
    // make sure function does not affect totals/per-game switch
    if (id.toLowerCase().indexOf("myswitch") === -1) {
        var elem = $(this);

        // if avg box gets checked
        var pattern1 = /add-player-avg-/;
        var suffix1 = this.id.match(/\d+/);

        //returns true or false...
        var exists1 = pattern1.test(id);
        if ((exists1) && (elem.is(":checked"))) {
            $('#add-player-total-' + suffix1).prop('checked', true)
            var values1 = Array($("input[name='select-checkbox']:checked").closest("td").siblings("td").text())
            // $.each($("input[name='select-checkbox']:checked").closest("td").siblings("td"),
            //     function () {
            //             values.push($(this).text());
            //     });
            // alert("val---" + values.join(", "));
            alert(values1)
            var values1_as_string = JSON.stringify(values1);
            var contains = values.some(function(ele){
                return JSON.stringify(ele) === values1_as_string;
              });

            values.push(values1)



        //true statement, do whatever
        } else if ((exists1) && (elem.not(":checked"))) {
            $('#add-player-total-' + suffix1).prop('checked', false)
            var values1 = Array($("input[name='select-checkbox']:checked").closest("td").siblings("td").text())
            values.push(values1)
        }
    }

        // if totals box gets checked
        var pattern2 = /add-player-total-/;
        var suffix2 = this.id.match(/\d+/);

        //returns true or false...
        var exists2 = pattern2.test(id);
        if ((exists2)  && (elem.is(":checked"))) {
            $('#add-player-avg-' + suffix2).prop('checked', true)
            var values2 = Array($("input[name='select-checkbox']:checked").closest("td").siblings("td").text())
            // $.each($("input[name='select-checkbox']:checked").closest("td").siblings("td"),
            //     function () {
            //             values.push($(this).text());
            //     });
            alert(values2)
            var values2_as_string = JSON.stringify(values2);
            var contains = values.some(function(ele){
                return JSON.stringify(ele) === values2_as_string;
              });
            values.push(values2)

        //true statement, do whatever
        } else if ((exists2) && (elem.not(":checked"))) {
            $('#add-player-avg-' + suffix2).prop('checked', false)
            var values2 = Array($("input[name='select-checkbox']:checked").closest("td").siblings("td").text())
            values.push(values2)
            
        }}
    );



$(document).ready(function () {
    $('#add-players-btn').click(function (e) {
        var $form = $('#playersform');
        var $checkbox = $('.select-checkbox');

        
        if (!$checkbox.is(':checked')) {
            alert('Please select !');
            $('#tipdivcontent').css("display", "block");
            e.preventDefault();
        }
        else
            var values_final = values[values.length -1]
            var values_final_split = JSON.stringify({'data':values_final.toString()})
            alert(values_final_split)

            const URL = '/'
            const xhr = new XMLHttpRequest();
            xhr.open('POST', URL);
            xhr.send(values_final_split);
            alert("working")

            const chunkSize = 25;
            // for (let i = 1; i < values_final_split.length; i += chunkSize) {
            //     const chunk = values_final_split.slice(i, i + chunkSize);
            //     alert(chunk)
            // }
            // $.ajax({
            //     type: "POST",
            //     url: "/",
            //     data: values_final_split,
            //     contentType: "application/json; charset=utf-8",
            //     dataType: "json",
            //     success: function (data) {
            //         alert(JSON.stringify(data));
            //     }
            // });
            // // $.post("/", {"myData": values_final_split})
            // $form.submit();
            
function doWork() {
    $.post("/", values_final_split, function(reply){
        $('#ajax_result').text(reply);
    });
        event.preventDefault();
}
        
    });            
});



function submit() {
    var myData = values[values.length -1]
    $.post("/", {"myData": myData})
}
