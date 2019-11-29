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



function togglecells2(that){
    alert("function fired")
}


function addColorToRows(td1) {


var list = td1;
     list.each(function(){

                if($(this).hasClass("EA"))
                {
                    $(this).addClass("eacellcolor");
                }
                else if ($(this).hasClass("SA"))
                {
                    $(this).addClass("sacellcolor");
                }
                else if ($(this).hasClass("Work"))
                {
                    $(this).addClass("wscellcolor");
                }
                else if ($(this).hasClass("Volunteer"))
                {
                    $(this).addClass("vtcellcolor");
                }
            });
}
function togglecells(targetcell,classname,tutorname) {

    var isMouseDown = false;


    $('[name=tb]')
        .on('mousedown', targetcell, function() {
            isMouseDown = true;


            if ($(this).hasClass(classname)) {
                $(this).removeClass(classname);
                this.innerHTML  = '';

            }
            else
            {   this.innerHTML = tutorname;
                $(this).addClass(classname);

            }
        })
        .on('mouseup', targetcell, function() {
            isMouseDown = false;
        })
        .on('mouseover', targetcell, function() {

            if (isMouseDown)
            {

                if ($(this).hasClass(classname)) {
                    $(this).removeClass(classname);
                                 this.innerHTML  = '';
                }
                else
                {
                    this.innerHTML = tutorname;
                    $(this).addClass(classname);

                }
            }
        })
        .on('mouseleave', function() {
            isMouseDown = false;
            if (isMouseDown) {

                $(this).removeClass(classname);
                this.innerHTML  = '';
            }

        })
    ;


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


function toggleinputs(targetcell,classname,tutorname) {

    var isMouseDown = false;


    $('[name=tb]')
        .on('mousedown', targetcell, function() {
            isMouseDown = true;


            if ($(this).hasClass(classname)) {
                $(this).removeClass(classname);
                $(this).value ("");

            }
            else
            {   this.value = tutorname;
                $(this).addClass(classname);

            }
        })
        .on('mouseup', targetcell, function() {
            isMouseDown = false;
        })
        .on('mouseover', targetcell, function() {

            if (isMouseDown)
            {

                if ($(this).hasClass(classname)) {
                    $(this).removeClass(classname);
                     $(this).value ("");
                }
                else
                {
                     $(this).value (tutorname);
                    $(this).addClass(classname);

                }
            }
        })
        .on('mouseleave', function() {
            isMouseDown = false;
            if (isMouseDown) {

                $(this).removeClass(classname);
                $(this).value ("");
            }

        })
    ;


}

function validateTime () {

		    var thisTime = this.value;
			var thisId = this.id;
		    var newID = thisId.replace("To", "From");
			var prevTime = document.getElementById(newID).value;

          if(thisTime != 0){
		      if(thisTime <= prevTime){
		        alert ( "time smaller than the previous. invalid");
			    this.value = 0;
		      }
	      }
}

function validateTime2 () {

		    var thisTime = this.value;
			var thisId = this.id;
		    var newID = thisId.replace("From", "To");
			var afterTime = document.getElementById(newID).value;

          if(afterTime != 0){
		      if(thisTime >= afterTime){
		        alert ( "time larger than the after. invalid");
			    this.value = 0;
		      }
  	      }
}


