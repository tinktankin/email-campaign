    function validateForm() {
  var x = document.forms["My"]["psw"].value;
  var y = document.forms["My"]["psw1"].value;


  if (x!=y) {
   alert("Password Not Matched");

  }
  else{

  $.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/passwordchnage/", /* django ajax posting url  */
       data: {
       type:'start',
        password: $('#psw').val(),
        id:$('#user_id').val(),
        res:$('#res').val(),
        csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')


       },

       success: function(data){
       if(data.is_created){
       alert('password reset');
       window.location.href="http://localhost:8000/TinkComm/login/";
       }
       if(data.is_done){
       alert('You already reset your password');
       }
       else if(data.is_invalid){
       alert('link is invalid');
       }
       },

       failure: function() {
            alert("Some error......");
       }



  });
}
}
