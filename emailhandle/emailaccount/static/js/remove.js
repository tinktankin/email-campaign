function remove(objButton){
var x=objButton.value;
$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/remove/", /* django ajax posting url  */
       data: {
       type:'start',
       button:x,
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){
      if(data.is_delete){
       alert("Delete");
       window.location.href="http://localhost:8000/TinkComm/user/accountsetting/";
       }
       },

       failure: function() {
            alert("Some error......");
       }

  });

}

function makedefault(obj){
var y=obj.value;
$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/makedefault/", /* django ajax posting url  */
       data: {
       type:'start',
       butt:y,
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){
       if(data.is_default){
       alert("Default");
       window.location.href="http://localhost:8000/TinkComm/user/accountsetting/";
       }
       },

       failure: function() {
            alert("Some error......");
       }

  });


}
function ACC(obj){
window.location.href="http://localhost:8000/TinkComm/user/account/changepassword/";
}
