    function validateForm() {
  var x = document.forms["My"]["psw"].value;
  var y = document.forms["My"]["psw1"].value;


  if (x!=y) {
   alert("Password Not Matched");

  }
  else{

  $.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/account/verify/password/", /* django ajax posting url  */
       data: {
       type:'start',
        password: $('#psw').val(),
        id:$('#id').val(),
        old:$('#old').val(),
        csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')


       },

       success: function(data){
       if(data.is_done){
       alert('password Change');
       window.location.href="http://localhost:8000/TinkComm/login/";
       }
       if(data.is_wrong){
       alert('Your Old password is not same as you enter error.......');
       }
       },

       failure: function() {
            alert("Some error......");
       }



  });
}
}
