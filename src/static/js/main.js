
jQuery(function($) {'use strict',





	// feed request
   $( "#submit_bt" ).click(function() {
            //get nick name
            var input = $("#name").val();
            //checking user input is not empty
            if (input.length==0){
            alert("please enter Nickname")
            return;
            }
            //msg diplsay
            $('#msg').css('display','block');
            /// empty varible to fill it with html elements
            html="";
            //ajax request to geet_feed
                    $.ajax({
                        url : "/get_feed/",
                        type : "GET",
                        dataType: "json",
                        data :{name:input,csrfmiddlewaretoken: '{{ csrf_token }}'},
                        success : function(data) {
                            if(data.length>0){
                            $.each(data, function( index, value ) {
                                obj={"id":value['id'],"text":value['text']};
                                html+="<li>"+JSON.stringify(obj,null,"  ")+"</li>";
                                //console.log(JSON.stringify(obj,null,"/t"));
                            });
                          // console.log(JSON.stringify(data,null,"/t"));

                            $(".tweets").html("");
                            $(".tweets").append(html);
                            }
                            else{
                            $(".tweets").html("This user have no tweets");
                            }
                            //removing msg
                            $('#msg').css('display','none');
                        },
                        error : function(xhr,errmsg,err) {
                           // alert(xhr.status + ": " + xhr.responseText);
                           alert("something went wrong please make sure the Nickname is valid")
                           //removing msg
                           $('#msg').css('display','none');
                        }
                    });

                    return false;

});




});






