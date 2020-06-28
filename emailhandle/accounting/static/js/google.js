// <script>
//@csrf_exempt
        function onSignIn(googleUser) {
            // Useful data for your client-side scripts:
            var profile = googleUser.getBasicProfile();
            var auth2 = gapi.auth2.getAuthInstance();
                  if(profile){
                            $.ajax({

                type: 'POST',

                url: 'http://localhost:8000/TinkComm/google/',

                data: {id:profile.getId(), name:profile.getName(), email:profile.getEmail(),csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')}

            }).done(function(data){

              if(data.is_taken){

              alert("Account alreday taken");
              auth2.signOut();
              }
              else if(data.is_created){
              alert("Account created");
              auth2.signOut();
              window.location.href="http://localhost:8000/TinkComm/user/home/";
              }

            }).fail(function() {

                alert( "Posting failed." );

            });
                var auth2 = gapi.auth2.getAuthInstance();
                auth2.signOut();
}
}
  //  </script>
