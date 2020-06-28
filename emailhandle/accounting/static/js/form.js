    function validateForm() {
  var x = document.forms["My"]["psw"].value;
  var y = document.forms["My"]["psw1"].value;
  var z=document.forms["My"]["user_id"].value;
  var e=document.forms["My"]["email"].value;
  var n=document.forms["My"]["name"].value;
  var c=document.forms["My"]["city"].value;

  if (x!=y) {
   alert("Password Not Matched");
    return false;
  }
}

