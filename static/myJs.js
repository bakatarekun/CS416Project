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

  // function togglecells(targetcell,classname) {
  //
  //               var isMouseDown = false;
  //
  //               $('[name=tb]')
  //                   .on('mousedown', targetcell, function() {
  //                       isMouseDown = true;
  //                       $(this).toggleClass(classname);
  //                   })
  //                   .on('mouseover', targetcell, function() {
  //                       if (isMouseDown)
  //                           $(this).addClass(classname);
  //                   })
  //                   .on('mouseup', targetcell, function() {
  //                       isMouseDown = false;
  //                   })
  //                   .on('mouseleave', function() {
  //                       isMouseDown = false;
  //                   });
  //
  //              $(targetcell).click( function() {
  //                   if (isMouseDown==false)
  //                       if($(this).hasClass(classname))
  //                       {      $(this).removeClass(classname);   }
  //                       else {
  //                            $(this).addClass(classname);
  //                       }
  //               })
  //           }

 function togglecells(targetcell,classname) {

                var isMouseDown = false;

                $('[name=tb]')
                    .on('mousedown', targetcell, function() {
                        isMouseDown = true;
                        if ($(this).hasClass(classname)) {
                                 $(this).removeClass(classname);
                             }
                             else
                            $(this).addClass(classname);
                    })
                    .on('mouseover', targetcell, function() {
                        if (isMouseDown)
                        {
                             if ($(this).hasClass(classname)) {
                                 $(this).removeClass(classname);
                             }
                             else
                            $(this).addClass(classname);
                        }
                    })
                    .on('mouseleave', function() {
                        if (isMouseDown) {

                                 $(this).removeClass(classname);

                         }
                        isMouseDown = false;
                    })
                    .on('mouseup', targetcell, function() {
                        isMouseDown = false;
                    });


            }
