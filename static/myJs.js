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



function togglecells(targetcell,classname,tutorname) {

    var isMouseDown = false;


    $('[name=tb]')
        .on('mousedown', targetcell, function() {
            isMouseDown = true;


            if ($(this).hasClass(classname)) {
                $(this).removeClass(classname);
                this.innerText = "";

            }
            else
            {   this.innerText = tutorname;
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
                    this.innerText = "";
                }
                else
                {
                    this.innerText = tutorname;
                    $(this).addClass(classname);

                }
            }
        })
        .on('mouseleave', function() {
            isMouseDown = false;
            if (isMouseDown) {

                $(this).removeClass(classname);
                this.innerText = "";
            }

        })
    ;


}



