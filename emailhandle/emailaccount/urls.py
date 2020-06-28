from django.conf.urls import url
from django.urls import path,include
from . import views
app_name="emailaccount"
urlpatterns=[
    path('accountsetting/',views.emailaccountsetting,name="accountsetting"),
    path('contact',views.contact,name="contact"),
    path('mailbox',views.mailbox,name="mailbox"),
    path('contactfile/',views.contactfile,name="contactfile"),
    path('uploadphoto/',views.userphoto,name="userphoto"),
    path('addemail/',views.addemail,name="addemail"),
    path('updatename/',views.changename,name="chnagename"),
    path('chnageemailpassword/',views.chnageemailpassword,name="emailpass"),
    path('makedefault/',views.makedefault,name="makedefault"),
    path('remove/',views.remove,name="remove"),
    path('account/changepassword/',views.chnageaccpassword,name="accpass"),
    path('account/verify/password/',views.verifychnagepassword,name="verify"),
    path('addcontact/',views.addcontacts,name="addaccount"),
    path('groups/',views.groups,name="groups"),

]
