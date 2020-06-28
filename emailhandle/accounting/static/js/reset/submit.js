function validateForm(){
$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/signup/", /* django ajax posting url  */
       data: {
       type:'start',
       name:$("#name").value(),
       userid:$("#user_id").value(),
       psw:$("#psw").value(),
       email:$("#email").value(),
       city:$("#city").value(),
       pass:$('#psw1').value(),
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){
       if(data.is_have){
       alert("Username alreday exists");
       return false;
       }
       else if(data.is_email){
       alert("email already exists");
       }
       else if(data.is_pass){
       alert("Password not matched");
       }
       else if(data.is_created){
       alert("User Created");
       window.location.href="http://localhost:8000/TinkComm/user/home/";
       }

       },

       failure: function() {
            alert("Some error......");
       }



  });


}
