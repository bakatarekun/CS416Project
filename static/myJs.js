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





 function togglecell(){
                $('td').click( function() {
                    $(this).toggleClass("red-cell");
                } );
            }

            function tobbleandhighlight() {
                var isMouseDown = false;

                $('[name=tb]')
                    .on('mousedown', 'td', function() {
                        isMouseDown = true;
                        $(this).toggleClass("red-cell");
                    })
                    .on('mouseover', 'td', function() {
                        if (isMouseDown)
                            $(this).addClass("red-cell");
                    })
                    .on('mouseup', 'td', function() {
                        isMouseDown = false;
                    })
                    .on('mouseleave', function() {
                        isMouseDown = false;
                    });

                $('td').click( function() {
                    if (isMouseDown==false)
                        $(this).toggleClass("red-cell");
                })
            };
