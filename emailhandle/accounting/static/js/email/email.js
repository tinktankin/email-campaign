function getemail(){
$.ajax({

                type: 'POST',

                url: 'http://localhost:8000/TinkComm/user/get_emailverify_url/',

                data: {type:'start',csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')}

            }).done(function(data){

              if(data.is_taken){

              alert("Email Send");
                return false;
              }
              if(data.done){

              alert("Email Verfication Alreday done");
                return false;
              }

            }).fail(function() {

                alert( "Posting failed." );
                return false;

            });


}
