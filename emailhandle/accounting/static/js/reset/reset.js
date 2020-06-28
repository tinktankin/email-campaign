$('#form').on('submit', function(e){

e.preventDefault();

  $.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/reset_email_password/", /* django ajax posting url  */
       data: {
       type:'start',
        email: $('#email').val(),
        csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')


       },

       success: function(data){
       if(data.is_taken){
       alert('password reset link send to your mail');
       }
       if(data.is_provider){
       alert('Sorry due to some security risk we dont reset your password');
       }
       if(data.is_created){
          alert("You are not a valid user");
           }/* response message */
       },

       failure: function() {
            alert("Some error......");
       }


   });


        });
