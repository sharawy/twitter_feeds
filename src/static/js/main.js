
jQuery(function($) {'use strict',





	// feed form
   $( "#submit_bt" ).click(function() {
            var input = $("#name").val();
            $('#msg').css('display','block');
            html="";
                    $.ajax({
                        url : "/get_feed/",
                        type : "GET",
                        dataType: "json",
                        data :{name:input,csrfmiddlewaretoken: '{{ csrf_token }}'},
                        success : function(data) {

                            $.each(data, function( index, value ) {
                                html+="<li>"+value['text']+"</li>";

                            });
                            console.log(html);
                            $(".tweets").html("");
                            $(".tweets").append(html);
                        },
                        error : function(xhr,errmsg,err) {
                           // alert(xhr.status + ": " + xhr.responseText);
                           alert("something went wrong")
                        }
                    });
                    $('#msg').css('display','none');
                    return false;

});




});






