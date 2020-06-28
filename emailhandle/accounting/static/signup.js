    function validateForm() {
  var x = document.forms["My"]["PASSWORD1"].value;
  var y = document.forms["My"]["PASSWORD2"].value;

  if (x!=y) {
    alert("Password Not Matched");
    return false;
  }

}
