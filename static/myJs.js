function ajaxcall() {


    temp = "/topics/" + temp;
    $.ajax({
        type: "GET",
        //url: "/topics/2",
        url: temp,
        // data: Course,
        dataType: "json",
        contentType: "application/json",
        success: function (data) {

            var str = data.id + " " + data.name + " " + data.description;

            $("#mydiv").text(str);


        },

        error: function () {

            alert("wasn't succesful");

        }
    });
}



function togglecells2(that) {
    alert("function fired")
}


function addColorToRows(td1) {


    var list = td1;
    list.each(function () {

        if ($(this).hasClass("EA")) {
            $(this).addClass("eacellcolor");
        } else if ($(this).hasClass("SA")) {
            $(this).addClass("sacellcolor");
        } else if ($(this).hasClass("Work")) {
            $(this).addClass("wscellcolor");
        } else if ($(this).hasClass("Volunteer")) {
            $(this).addClass("vtcellcolor");
        }
    });
}

function togglecells(targetcell, classname, tutorname) {

    var isMouseDown = false;


    $('[name=tb]')
        .on('mousedown', targetcell, function () {
            isMouseDown = true;


            if ($(this).hasClass(classname)) {
                $(this).removeClass(classname);
                this.innerHTML = '';

            } else {
                this.innerHTML = tutorname;
                $(this).addClass(classname);

            }
        })
        .on('mouseup', targetcell, function () {
            isMouseDown = false;
        })
        .on('mouseover', targetcell, function () {

            if (isMouseDown) {

                if ($(this).hasClass(classname)) {
                    $(this).removeClass(classname);
                    this.innerHTML = '';
                } else {
                    this.innerHTML = tutorname;
                    $(this).addClass(classname);

                }
            }
        })
        .on('mouseleave', function () {
            isMouseDown = false;
            if (isMouseDown) {

                $(this).removeClass(classname);
                this.innerHTML = '';
            }

        });


}

// function togglecells(targetcell,classname,tutorname) {
//
//     var isMouseDown = false;
//
//
//     $('[name=tb]')
//         .on('mousedown', targetcell, function() {
//             isMouseDown = true;
//
//
//             if ($(this).hasClass(classname)) {
//                 $(this).removeClass(classname);
//                 this.innerHTML = "";
//
//             }
//             else
//             {   this.innerHTML = tutorname;
//                 $(this).addClass(classname);
//
//             }
//         })
//         .on('mouseup', targetcell, function() {
//             isMouseDown = false;
//         })
//         .on('mouseover', targetcell, function() {
//
//             if (isMouseDown)
//             {
//
//                 if ($(this).hasClass(classname)) {
//                     $(this).removeClass(classname);
//                     this.innerHTML = "";
//                 }
//                 else
//                 {
//                     this.innerHTML = tutorname;
//                     $(this).addClass(classname);
//
//                 }
//             }
//         })
//         .on('mouseleave', function() {
//             isMouseDown = false;
//             if (isMouseDown) {
//
//                 $(this).removeClass(classname);
//                 this.innerHTML = "";
//             }
//
//         })
//     ;
//
//
// }


function toggleinputs(targetcell, classname, tutorname) {

    var isMouseDown = false;


    $('[name=tb]')
        .on('mousedown', targetcell, function () {
            isMouseDown = true;


            if ($(this).hasClass(classname)) {
                $(this).removeClass(classname);
                $(this).value("");

            } else {
                this.value = tutorname;
                $(this).addClass(classname);

            }
        })
        .on('mouseup', targetcell, function () {
            isMouseDown = false;
        })
        .on('mouseover', targetcell, function () {

            if (isMouseDown) {

                if ($(this).hasClass(classname)) {
                    $(this).removeClass(classname);
                    $(this).value("");
                } else {
                    $(this).value(tutorname);
                    $(this).addClass(classname);

                }
            }
        })
        .on('mouseleave', function () {
            isMouseDown = false;
            if (isMouseDown) {

                $(this).removeClass(classname);
                $(this).value("");
            }

        });


}

// function validateTime () {

//     var thisTime = this.value;
//     var thisId = this.id;
//     var newID = thisId.replace("To", "From");
//     var prevTime = document.getElementById(newID).value;

//   if(thisTime != 0){
//       if(thisTime <= prevTime){
//         alert ( "time smaller than From. invalid");
//         this.value = 0;
//       }
//   }
// }

function validateTime() {

    var thisTime = this.value;
    var thisId = this.id;
    var newID = thisId.replace("To", "From");
    var prevTime = document.getElementById(newID);

    if (prevTime.value != 0) {
        if (thisTime <= prevTime.value) {
            alert("time smaller than From. invalid");
            this.value = 0;
        }
    }
    //  else {
    //     if (prevTime.value == 0) {
    //         alert("prev time can't be empty");
    //         prevTime.focus();
    //     }
    // }
}

function validateTime2() {

    var thisTime = this.value;
    var thisId = this.id;
    var newID = thisId.replace("From", "To");
    var afterTime = document.getElementById(newID);

    if (afterTime.value != 0) {
        if (thisTime >= afterTime.value) {
            alert("time larger than To. invalid");
            this.value = 0;
        }

    }
}


function test() {

    alert("testing static file");
}

function makerows(tutors) {

    var setoftutors = tutors;
    var counter = 9;
    var rowcounter = 0;
    var hours;

    var listoftutors = '<ul>'
    listoftutors += '<h3>Tutor\'s Hours and Availabilities</h3>'

    for (s = 0; s < setoftutors.length; s++) {

        var name = setoftutors[s].fields.tutor[0];
        var timefrom1 = setoftutors[s].fields.From1;
        var timeto1 = setoftutors[s].fields.To1;
        var typeofemployee = setoftutors[s].fields.tutor[1];
        var usedHours = setoftutors[s].fields.tutor[3];
        hours = setoftutors[s].fields.tutor[2];

        if (typeofemployee == 'EA') {
            togglecells("td[name=" + name + "]", "eacellcolor", name);
        } else if (typeofemployee == 'SA') {
            togglecells("td[name=" + name + "]", "sacellcolor", name);
        } else if (typeofemployee == 'Work Study') {
            togglecells("td[name=" + name + "]", "wscellcolor", name);
        } else {
            togglecells("td[name=" + name + "]", "vtcellcolor", name);
        }

        listoftutors += '<li style="font-size: x-large"><input type="hidden" name="usedHours" id=' + name + 'input' + '><span name="spanname">' + name + '</span><span style="padding-left:5px" name="spanhours" id=' + name + '></span> Hrs --' + '<span> Left<span style="padding-left:5px" name="spanhourstotal" id=' + name + 'total' + ' \'>' + usedHours + '</span> Hrs: From ' + timefrom1 + ' To ' + timeto1 + '</span></li>'
    }

    listoftutors += '</ul><br>';
    $('#listoftutors').append(listoftutors);

    displayHours(setoftutors);
    saveAccumulatedHours(setoftutors, accumulatedHours);
    displayHours2(setoftutors);

    $('tr td[name!="delRow"]').mouseleave(function () {



        displayHours2(setoftutors);
        saveAccumulatedHours(setoftutors, accumulatedHours);

    });
}

function displayHours(setoftutors) {
    var name1;
    var usedhours;
    var nameid;
    var nameinput;
    var usedhoursfromDB;
    for (s = 0; s < setoftutors.length; s++) {

        name1 = setoftutors[s].fields.tutor[0];

        nameid = "#" + name1;
        nameinput = "#" + name1 + "input";
        usedhoursfromDB = parseFloat(setoftutors[s].fields.tutor[3]);
        usedhours = ($("td:contains(" + name1 + ")").length - 1) * .5;

        $(nameid).text(usedhours);
        $(nameinput).val(usedhours);
        $('input[id =' + name1 + ']').val(usedhours);
    }


}

function displayHours2(setoftutors) {
    var name1;
    var usedhours;
    var hours2;
    var nameid;
    var nameinput;
    var usedhoursfromDB;
    var spantotalHours;
    for (s = 0; s < setoftutors.length; s++) {

        name1 = setoftutors[s].fields.tutor[0];
        nameid = "#" + name1;
        nameinput = "#" + name1 + "input";
        usedhoursfromDB = parseFloat(setoftutors[s].fields.tutor[3]);
        usedhours = ($("td:contains(" + name1 + ")").length - 1) * .5;
        spantotalHours = "#" + name1 + "total";
        $(nameid).text(usedhours);
        $('input[id =' + name1 + ']').val(usedhours);

    }

    var usedHours = [];
    var result;
    // alert(accumulatedHours);
    $("input[name='usedHours']").each(function (index) {
        usedHours[index] = $(this).val();

    });
    var namelist = $('span[name="spanname"]');
    for (i = 0; i < namelist.length; i++) {
        var n = namelist[i].innerHTML;
        var h = usedHours[i];
        var usedhoursfromDB = accumulatedHours[i];
        var currentHours = ($("td:contains(" + n + ")").length - 1) * .5;
        h = usedhoursfromDB - (h - currentHours);
        hours2 = setoftutors[i].fields.tutor[2];
        h = hours2 - h;


        var spantotalHours = "#" + n + "total";
        if (h <= 0) {

            $(spantotalHours).css({
                "color": "red"
            });
        } else {
            $(spantotalHours).css({
                "color": "black"
            });
        }
        $(spantotalHours).text(h);
    }


}

function saveAccumulatedHours(setoftutors, accumulatedHours) {
    var name1;
    var usedhours;

    for (s = 0; s < setoftutors.length; s++) {
        var usedhoursfromDB = parseFloat(setoftutors[s].fields.tutor[3]);
        accumulatedHours[s] = usedhoursfromDB;
    }
}



function getUsedHoursAndName(setoftutors) {
    var usedHours = [];
    var result;
    // alert(accumulatedHours);
    $("input[name='usedHours']").each(function (index) {
        usedHours[index] = $(this).val();

    });

    var namelist = $('span[name="spanname"]');

    for (i = 0; i < namelist.length; i++) {
        var n = namelist[i].innerHTML;
        var h = usedHours[i];
        var usedhoursfromDB = accumulatedHours[i];
        var currentHours = ($("td:contains(" + n + ")").length - 1) * .5;

        h = usedhoursfromDB - (h - currentHours);
        result = saveUsedHours(n, h);

    }
    if (result) {
        alert("hours saved");
    }
}


function saveUsedHours(name, usedhours) {
    var result = true;
    $.ajax({
        type: "GET",
        url: "/saveUsedHours",
        dataType: "text",
        data: {
            "name": name,
            "usedhours": usedhours
        },
        contentType: "application/json",
        success: function () {

        },

        error: function () {

            alert("wasn't succesful");
            result = false;

        }
    });
    return result;
}

function saveSchedule(tutorname, day) {
    var schedule = [];
    var tutorname2 = tutorname
    $("td[name=" + tutorname2 + "]").each(function (index) {
        schedule[index] = $(this).text();
    });

    $.ajax({
        type: "GET",
        url: "/saveSchedule",
        dataType: "text",
        data: {
            "schedule": schedule,
            "tutorname": tutorname2,
            "day": day
        },
        contentType: "application/json",
        success: function () {


        },

        error: function () {

            alert("wasn't succesful");

        }
    });

}

function saveAllSchedule() {
    getUsedHoursAndName();
    var day = $('#dayinputhidden').val();
    var namelist = $('span[name="spanname"]');

    for (i = 0; i < namelist.length; i++) {
        var n = namelist[i].innerHTML;
        saveSchedule(n, day);
    }
    alert("scheduel saved succesfully");
}

function adjustTimeSelect(thisobj, begin, end) {
    var timeList = document.getElementById(thisobj);
    for (var i = begin; i < end; i++) {
        timeList[i].style.display = "none";
    }
}

function adjustTimeSelectFri(thislist) {


    for (var i = 15; i < thislist.length; i++) {
        thislist[i].style.display = "none";
    }

}

function adjustTimeSelectSat(thislist) {

    for (let i = 1; i < 2; i++) {
        thislist[i].style.display = "none";
    }

    for (let i = 13; i < thislist.length; i++) {
        thislist[i].style.display = "none";
    }

}

function adjustTimeSelectSun(thislist) {

    for (let i = 1; i < 6; i++) {
        thislist[i].style.display = "none";
    }

    for (let i = 15; i < thislist.length; i++) {
        thislist[i].style.display = "none";
    }

}

// function checkRequiredField() {

//     var isPassed = true;
//     var t = jQuery('select[id*="From1"]');
//   // var t = jQuery(fromField);
//     for (i = 0; i < t.length; i++) {

//         if (t[i].value != 0) {

//             let newID = t[i].id.replace("From", "To");
//             let afterTime = document.getElementById(newID);;
//             if (afterTime.value == 0) {
//                 isPassed = false;
//                 alert("one of the fields is missing");
//                 afterTime.focus();
//                 return isPassed;
//             }

//         } else if (t[i].value == 0) {

//             let newID2 = t[i].id.replace("From", "To");
//             let afterTime2 = document.getElementById(newID2);

//             if (afterTime2.value != 0) {
//                 isPassed = false;
//                 alert("one of the fields is missing");
//                 t[i].focus();
//                 return isPassed;
//             }


//         }

//     }
//     return isPassed;
// }

function checkRequiredField() {
 //debugger;

    var reuslt1= true;
    var reuslt2= true;
    result1 = checkFields('select[id*="From1"]');
    //  if (result1 == false)
    //  {
    //     return result1;

    //  }
    //  else
    //  {
    //     result2 = checkFields('select[id*="From2"]');
    //     if( reuslt1 == true && reuslt2 == true)
    //     {
    //         return true;
    //     }
    //     else
    //     {
    //         return false;
    //     }
    //  }



    return result1;
}

function checkFields(fromField) {
   // debugger;
    var isPassed = true;
    var t = jQuery(fromField);
    for (i = 0; i < t.length; i++) {

        if (t[i].value != 0) {

            let newID = t[i].id.replace("From", "To");
            let afterTime = document.getElementById(newID);;
            if (afterTime.value == 0) {
                isPassed = false;
                alert("one of the fields is missing");
                afterTime.focus();
                return isPassed;
            }

        } else if (t[i].value == 0) {

            let newID2 = t[i].id.replace("From", "To");
            let afterTime2 = document.getElementById(newID2);

            if (afterTime2.value != 0) {
                isPassed = false;
                alert("one of the fields is missing");
                t[i].focus();
                return isPassed;
            }


        }

    }
    return isPassed;

}

