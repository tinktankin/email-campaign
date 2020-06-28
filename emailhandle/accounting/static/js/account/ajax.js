function logout(){

$.ajax({
       type : "POST",
       url: "http://localhost:8000/TinkComm/logout/", /* django ajax posting url  */
       data: {
       type:'start',
       csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')
       },

       success: function(data){

       window.location.href="http://localhost:8000/TinkComm/login/";
       },

       failure: function() {
            alert("Some error......");
       }



  });

}
