import random
import string
from datetime import timedelta

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
import requests
from django.core.mail import send_mail
import json
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
#from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from cryptography.fernet import Fernet
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.timezone import datetime
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from accounting.tokens import account_activation_token, password_reset_token

from .forms import Accountform
# Create your views here.
from .models import Account, Session,Accountdetail,EmailAccounts
#from django.contrib.auth import authenticate
#pythom
#key = Fernet.generate_key() #this is your "password"
from emailhandle import settings

cipher_suite = Fernet(settings.ENCRYPT_KEY)
c_suite=Fernet(settings.ENCRYPT_KEY2)
c_suite2=Fernet(settings.ENCRYPT_KEY3)
def home(request):
    return render(request,'accounting/home.html',locals())
def logout(request):
    l=request.POST.get('type')
    if l=="start":
        if not request.session.session_key:
            request.session.save()
        s=request.session._session_key
        se=Session.objects.filter(session_key=s)
        se.delete()
        return redirect('accounting:login')
    else:
        return HttpResponse("Invalid Link")

##SignUp
def signup(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if Account.objects.filter(pk=k).exists():
        return redirect('accounting:userhome')
        #return HttpResponse(k)
    else:
        return render(request,'accounting/signup1.html',locals())
########signup
def usersignup(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    type=request.POST.get("type")
    if type=="start":
        name=request.POST.get('name')
    username=request.POST.get('userid')
    upassword=request.POST.get('psw')
    email=request.POST.get('email')
    city=request.POST.get('city')
    pass2=request.POST.get('psw1')
    clientKey=request.POST['g-recaptcha-response']
    secretKey='6LfAfaoZAAAAAN2FnTq2qKnhpaMy9_4M6afcXYZ2'
    captchadata={
        'secret':secretKey,
        'response':clientKey
    }

    if name is not None:
        r=requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
        response=json.loads(r.text)
        verify=response['success']
        if verify==False:
            return render(request,'accounting/signup1.html',{'error_message67':"error"})
        if Account.objects.filter(username=username).exists():
            return render(request,'accounting/signup1.html',{'error_message':"error"})
        elif Account.objects.filter(email=email).exists():
            return render(request,'accounting/signup1.html',{'error':"error"})
        elif upassword!=pass2:
            return render(request,'accounting/signup1.html',{'error_message':"error"})
            #return render(request,'signup1.html',{'e_message':'Email alreday exists'})
        else:
            p=make_password(upassword)
            Account.objects.create(name=name,username=username,email=email,password=p,created_on=datetime.now())
            ac_id=Account.objects.get(name=name,username=username,email=email)
            ac_id=str(ac_id.id)
            ac_detail=Accountdetail.objects.filter(acc_id=ac_id)
            ac_detail.update(city=city)
            create_session(s,ac_id)
            return redirect('accounting:userhome')

    else:
        return HttpResponse("Wrong Url")
###Google SignUp
def google(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    name=request.POST.get('name')
    id=request.POST.get('id')
    email=request.POST.get('email')
    if name is not None:
        if Account.objects.filter(email=email):
            data={
                'is_taken':'Already taken '
            }
            return JsonResponse(data)
        else:
            e=email.split('@')
            username=e[0]
            p=False
            while p==False:
                if Account.objects.filter(username=username).exists():
                    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 5))
                    username=username+res
                    p=False
                else:
                    p=True
            Account.objects.create(provider="Google",username=username,name=name,email=email,token_id=id,created_on=datetime.now())
            account=Account.objects.get(provider="Google",name=name,email=email,token_id=id)
            ac_id=str(account.id)
            #account_detail=Accountdetail.objects.filter(acc_id=ac_id)
            #account_detail.update(everify=True)
            create_session(s,ac_id)
            data={
                'is_created':"Account created"
            }
            return JsonResponse(data)
    return HttpResponse("Wrong Url")

###Facebook signup
def fbtest(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    name=request.POST.get('name')
    id=request.POST.get('id')
    email=request.POST.get('email')
    if name is not None:
        if Account.objects.filter(email=email):
            data={
                'is_taken':'Already taken '
            }
            return JsonResponse(data)
        else:
            e=email.split('@')
            username=e[0]
            p=False
            while p==False:
                if Account.objects.filter(username=username).exists():
                    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 5))
                    username=username+res
                    p=False
                else:
                    p=True
            Account.objects.create(provider="Facebook",username=username,name=name,email=email,token_id=id,created_on=datetime.now())
            account=Account.objects.get(provider="Facebook",name=name,email=email,token_id=id)
            ac_id=str(account.id)
            #account_detail=Accountdetail.objects.filter(acc_id=ac_id)
            #account_detail.update(everify=True)
            create_session(s,ac_id)
            data={
                'is_created':"Account created"
            }
            return JsonResponse(data)
    return HttpResponse("Wrong Url")
###To know there is session of not in Database
def findkey(s):
    if Session.objects.filter(session_key=s):
        session_get=Session.objects.get(session_key=s)
        email_id=session_get.session_id
        decoded=email_id.encode()
        decoded_text = cipher_suite.decrypt(decoded)
        e=decoded_text.decode()
        return e
    else:
        return None
###Session id creation
def create_session(s,ac_id):
    encode=ac_id.encode()
    encoded_text = cipher_suite.encrypt(b"%s"%(encode))
    encoded_email=encoded_text.decode("utf-8")
    if Session.objects.filter(session_key=s).exists():
        return None
    else:
        Session.objects.create(createid=ac_id,session_id=encoded_email,session_key=s)
###Self usercreation
#def create_user(request):

####LOGIN
def login(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        if Account.objects.filter(pk=k).exists():
            return redirect('accounting:userhome')
    username=request.POST.get("userid")
    passwordgiven=request.POST.get("psw")
    if username is not None:
        print("hello")
        try:
            account=Account.objects.get(username=username)
            if account.provider is None:
                k=check_password(passwordgiven,account.password)
                if k is True:
                    ac_id=str(account.id)
                    create_session(s,ac_id)
                    return redirect('accounting:userhome')
                else:
                    return render(request,'accounting/login1.html',{'error_message':'wrong username and password'})
            else:
                return render(request,'accounting/login1.html',{'e_message':'your are not authenticated as this type og login'})
        except:
            return render(request,'accounting/login1.html',{'u_message':'wrong username or password'})
    else:
        return render(request,'accounting/login1.html',locals())


###Google Login
def googlelogin(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    name=request.POST.get('name')
    id=request.POST.get('id')
    email=request.POST.get('email')
    if name is not None:
        if Account.objects.filter(provider="Google",email=email,token_id=id).exists():
            account=Account.objects.get(provider="Google",name=name,email=email,token_id=id)
            ac_id=str(account.id)
            create_session(s,ac_id)
            data={
                'is_taken':'Log in'
            }
            return JsonResponse(data)
        else:
            data={
                'is_created':"create account first"
            }
            return JsonResponse(data)
    return HttpResponse("Wrong Url")
####Facebook Login
def facebooklogin(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    name=request.POST.get('name')
    id=request.POST.get('id')
    email=request.POST.get('email')
    if name is not None:
        if Account.objects.filter(email=email,token_id=id).exists():
            account=Account.objects.get(provider="Facebook",name=name,email=email,token_id=id)
            ac_id=str(account.id)
            create_session(s,ac_id)
            data={
                'is_taken':'Log in '
            }
            return JsonResponse(data)
        else:
            data={
                'is_created':"Create account first"
            }
            return JsonResponse(data)
    return HttpResponse("Wrong Url")
###to check database
def check_database(k):
    a=Accountdetail.objects.get(acc_id=k)
    if  a.city==None:
        return "form"
    if a.everify==False:
        return "email"
    if EmailAccounts.objects.filter(e_id=k).exists():
        return None
    else:
        return 'account'

    #return None
##to complete the required forms
def complete_form(request):

    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        check=check_database(k)
        if check=="form" and Account.objects.filter(pk=k).exists():
            city=request.POST.get('city')
            if city is not None:
                ad=Accountdetail.objects.filter(acc_id=k)
                adg=Accountdetail.objects.get(acc_id=k)
                ad.update(city=city)
                if adg.everify==True:
                    ad.update(comlpeted=True)
                return redirect('accounting:userhome')
            else:
                return HttpResponse("You are showing thi error because you are trying....")
        else:
            return redirect('accounting:userhome')
    else:
        return redirect('accounting:login')

####To return to pages which is required to compplete the total forms
def complete_test(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        try:
            a=Account.objects.get(pk=k)
            check=check_database(k)
            n=a.name
            name=n.split(' ')
            name=name[0]
            para={'username':a.username,'email':a.email,'name':name}
            if check=="form":
                return render(request,'accounting/completeform.html',para)
            if check=="email":
                return render(request,'accounting/emailverify.html',para)
            if check=="account":
                return redirect('emailaccount:accountsetting')
            else:
                return redirect('accounting:userhome')
        except:
            return redirect('accounting:login')
    else:
        return redirect('accounting:login')
###gives the dashboard page of user
def user_home(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        check=check_database(k)
        if check is not None:
            return redirect('accounting:complete_test')
        else:
            a=Account.objects.get(pk=k)
            n=a.name
            name=n.split(' ')
            name=name[0]
            para={'username':a.username,'email':a.email,'name':name}
            return render(request,'accounting/dashboard.html',para)
    else:
        return redirect('accounting:login')
#####Use to get the links for email verifications
def get_emailverify_link(request):
    t=request.POST.get("type")
    if t=="start":
        if not request.session.session_key:

            request.session.save()
        s=request.session._session_key
        k=findkey(s)
        if k is not None:
            a=Account.objects.get(pk=k)
            ac=Accountdetail.objects.get(pk=k)
            if ac.everify==True:
                data={
                    'done':'given'
                }
                return JsonResponse(data)
            ids=str(a.id)
            encoded_id=ids.encode()
            encoded_id_text=c_suite.encrypt(b"%s"%(encoded_id))
            encoded_id=encoded_id_text.decode("utf-8")
            ac_detail=Accountdetail.objects.filter(acc_id=ids)
            res = ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k = 9))
            res_make=make_password(res)
            ac_detail.update(date=datetime.now(),potp=res_make)
            current_site=get_current_site(request)
            message=render_to_string('accounting/account_activation_eamil.html',{
                'user':a,
                'domian':current_site.domain,
                'uid':encoded_id,
                'token':account_activation_token.make_token(a),
                'res':res,
            })
            subject="Your activation link for connect"
            #send_mail(subject,message,EMAIL_HOST_USER,[email], fail_silently = False)
            print(message)
            data={
                    'is_taken':'Log in'
                }
            return JsonResponse(data)
        else:
            return redirect('accounting:login')
    else:
        return HttpResponse("Invalid Link")

###To check the emaillink is Verified or not
def activate(request, uidb64, token,res):
    try:
        decoded=uidb64.encode()
        decoded_text = c_suite.decrypt(decoded)
        e=decoded_text.decode()
        a=Account.objects.get(pk=e)
        user=a
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(a, token):
        user_id=user.id
        account=Accountdetail.objects.filter(acc_id=user_id)
        acc=Accountdetail.objects.get(acc_id=user_id)
        if acc.everify==True:
            return HttpResponse("%s\nYour account already verified<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>"%(a.username))
        check=check_password(res,acc.potp)
        t=acc.date
        tim=datetime.now(timezone.utc)
        times=tim+timedelta(hours=5.5)
        diff=times-t
        minutes=divmod(diff.seconds,60)
        m=minutes[0]
        if m>30:
            return HttpResponse("Activation link is invalid<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>")
        if check==True:
            if acc.everify==True or acc.city is not None:
                    account.update(comlpeted=True)
            account.update(everify=True,potp=None)
            return HttpResponse("Your email verified now<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>")
        else:
            return HttpResponse("Your link is invalid<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>")
    else:
        return HttpResponse('Activation link is invalid!')
#####To reset the password:
def reset_password(request):
    return render(request,'accounting/reset_password.html',locals())
####get password reset mail
def reset_get_email(request):
    k=request.POST.get('type')
    if k=='start':
        email=request.POST.get('email')
        if Account.objects.filter(email=email).exists():
            account=Account.objects.get(email=email)
            if account.provider is None:
                ids=str(account.id)
                encoded_id=ids.encode()
                encoded_id_text=c_suite2.encrypt(b"%s"%(encoded_id))
                encoded_id=encoded_id_text.decode("utf-8")
                ac_detail=Accountdetail.objects.filter(acc_id=ids)
                res = ''.join(random.choices(string.ascii_uppercase +
                            string.digits, k = 10))
                res_make=make_password(res)
                ac_detail.update(date=datetime.now(),rotp=res_make)
                current_site=get_current_site(request)
                message=render_to_string('accounting/password_reset_email.html',{
                    'user':account,
                    'domian':current_site.domain,
                    'uid':encoded_id,
                    'token':password_reset_token.make_token(account),
                    'res':res,
                })
                #send_mail(subject,message,EMAIL_HOST_USER,[email], fail_silently = False)
                print(message)
                data={
                    'is_taken':'Log in'
                }
                return JsonResponse(data)

            else:
                data={
                    'is_provider':"yes"
                }
                return JsonResponse(data)
        else:
            data={
                'is_created':"hello"
            }
            return JsonResponse(data)
    else:
        return HttpResponse('This error comes because you call the url before the submit the passsword')
#####create a new password
def createnewpassword(request,uidb64, token,res):
    try:
        decoded=uidb64.encode()
        decoded_text = c_suite2.decrypt(decoded)
        e=decoded_text.decode()
        account=Account.objects.get(pk=e)
        user=account
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and password_reset_token.check_token(account, token):
        user_id=user.id
        account=Accountdetail.objects.filter(acc_id=user_id)
        acc=Accountdetail.objects.get(acc_id=user_id)
        #if acc.everify==True:
         #   return HttpResponse("%s\nYour account already verified<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>"%(a.username))
        if acc.rotp is None:
            return redirect('accounting:login')
        check=check_password(res,acc.rotp)
        t=acc.date
        tim=datetime.now(timezone.utc)
        times=tim+timedelta(hours=5.5)
        diff=times-t
        minutes=divmod(diff.seconds,60)
        m=minutes[0]
        if m>30:
            return HttpResponse("link is invalid<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>")
        if check==True:
            return render(request,'accounting/password.html',{'user_id':user_id,'res':res})
        else:
            return HttpResponse("Your link is invalid<br><a href='http://localhost:8000/TinkComm/login'>Go To Login</a>")
    else:
        return HttpResponse('Activation link is invalid!')
######last method to call the chnage pass
def changeit(request):
    t=request.POST.get('type')
    if t=='start':
        res=request.POST.get('res')
        id=request.POST.get('id')
        password=request.POST.get('password')
        acc=Accountdetail.objects.filter(acc_id=id)
        ac=Accountdetail.objects.get(acc_id=id)
        if ac.rotp is None:
            data={
                'is_done':'not verified'
            }
            return JsonResponse(data)
        check=check_password(res,ac.rotp)
        if check==True:
            password_hash=make_password(password)
            a=Account.objects.filter(pk=id)
            a.update(password=password_hash)

            acc.update(rotp=None)
            data={
            'is_created':'done'
            }
            if Session.objects.filter(createid=id).exists():
                s=Session.objects.filter(createid=id)
                s.delete()

            return JsonResponse(data)
        else:
            data={
                'is_invalid':'i'
            }
            return JsonResponse(data)
    else:
        return HttpResponse('Something wrong..........')
####--End of login logout and reset password email verification---###
### do not share the encrypted keys ---####
### use your own facebook and google api keys###
###i have upload with secret key and encrpted keys but in future if you want to upload don't share the keys
####------Naman Sharma------####
