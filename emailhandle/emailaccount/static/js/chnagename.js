function chnagename(){
  var x = document.forms["nameform"]["newname"].value;
  //var i=document.forms["nameform"]["id"].value;
$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/user/updatename/", /* django ajax posting url  */
       data: {
       type:'start',
       name:x,
       id:$('#id').val(),
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){
       if(data.is_change){
       alert("Name Change");
       }
       },

       failure: function() {
            alert("Some error......");
       }

  });





}
