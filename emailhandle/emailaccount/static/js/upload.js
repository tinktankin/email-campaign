function Upload(){
  var x = document.forms["My"]["newemailpassword"].value;
  var y = document.forms["My"]["confirmnewemailpassword"].value;
  var s=document.forms["My"]["selectprovider"].value;
  var e=document.forms["My"]["newemailid"].value;
  var z=document.forms["My"]["id"].value;

  if (x!=y) {
    alert("Password Not Matched");
    return false;
  }
else{
$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/addemail/", /* django ajax posting url  */
       data: {
       type:'start',
       id:z,
       provider:s,
       email:e,
       password:x,
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){
       if(data.is_have){
       alert("The email is already exists");
       }
       else{
       alert("Email added");
       window.location.href="http://localhost:8000/TinkComm/user/accountsetting/";
       }
       },

       failure: function() {
            alert("Some error......");
       }



  });





}
}
