function chnagepassword(){

  var x = document.forms["Change"]["newpassword"].value;
  var y = document.forms["Change"]["confirmpassword"].value;
  var s=document.forms["Change"]["selectemailid"].value;
  var e=document.forms["Change"]["oldpassword"].value;
  var z=document.forms["Change"]["id"].value;

//  var x = document.forms["nameform"]["newname"].value;

  //var i=document.forms["nameform"]["id"].value;

  if (x!=y) {
    alert("Password Not Matched");
    return false;
  }
  else{
$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/chnageemailpassword/", /* django ajax posting url  */
       data: {
       type:'start',
       email:s,
       password:x,
       old:e,
       id:z,
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){
       if(data.is_done){
       alert("Old password is Incorrect");
       }
       else{
       alert("Password Change");
       }
       },

       failure: function() {
            alert("Some error......");
       }

  });





}
}
