from django.conf.urls import url
from django.urls import path,include
from . import views
app_name="accounting"
urlpatterns=[

    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('google/',views.google,name="g"),
    path('f/',views.fbtest,name="f"),
    path('google/login/',views.googlelogin,name="googlelogin"),
    path('facebook/login/',views.facebooklogin,name="facebooklogin"),
    path('user/home/incomplete',views.complete_test,name="complete_test"),
    path('user/home/',views.user_home,name="userhome"),
    path('user/completeform',views.complete_form,name="completeform"),
    path('user/get_emailverify_url/',views.get_emailverify_link,name="emailverify"),
    path('activate_eamil/<uidb64>/<token>/<res>/',views.activate,name="activate"),
    path('reset_password/',views.reset_password,name="reset_password"),
    path('user/reset_email_password/',views.reset_get_email,name="resetpassword"),
    path('user/create_new_password/<uidb64>/<token>/<res>/',views.createnewpassword,name="newpassword"),
    path('user/passwordchnage/',views.changeit,name="chnageit"),
    path('user/signup/',views.usersignup,name="usersignup"),

]
