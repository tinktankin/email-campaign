//<script>

  function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    if (response.status === 'connected') {
      testAPI();
    } else {
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this webpage.';
    }
  }


  function checkLoginState() {               // Called when a person is finished with the Login Button.
    FB.getLoginStatus(function(response) {   // See the onlogin handler
      statusChangeCallback(response);
    });
  }


  window.fbAsyncInit = function() {
    FB.init({
      appId      : '1642677725890561',
      cookie     : true,
      xfbml      : true,
      version    : 'v7.0'
    });


    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  };


  (function(d, s, id) {                      // Load the SDK asynchronously
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));


  function testAPI() {                      // Testing Graph API after login.  See statusChangeCallback() for when this call is made.
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me?fields=name,email,id', function(response) {
     // console.log('Successful login for: ' + response.name);
      $.ajax({

                type: 'POST',

                url: 'http://localhost:8000/TinkComm/facebook/login/',

                data: {id:response.id,email:response.email,name:response.name,csrfmiddlewaretoken:$('meta[name="_token"]').attr('content')},

            }).done(function(data){

              if(data.is_taken){
              FB.logout(function(response){
          setElements(false);

      });
              window.location.href="http://localhost:8000/TinkComm/user/home/";


              }
                 else if(data.is_created){
                 FB.logout(function(response){
          setElements(false);

      });
              alert("Create a account first");
               }



            }).fail(function() {

                alert( "Posting failed." );

            });

    });

  }
   // </script>
