from cryptography.fernet import Fernet
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from emailhandle import settings
from accounting.models import Account, Accountdetail, EmailAccounts, ContactlistFile, Contactlist, Session
# Create your views here.
from accounting.views import check_database,findkey
from emailaccount.forms import FileUploadForm,PhotoUploadForm
Cipher_suites=Fernet(settings.ENCRYPT_KEY4)
def emailaccountsetting(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        form=PhotoUploadForm
        a=Account.objects.get(pk=k)
        acdetail=Accountdetail.objects.get(acc_id=k)
        check=check_database(k)
        n=a.name
        name=n.split(' ')
        name=name[0]
        if EmailAccounts.objects.filter(e_id=k).exists():
            e=EmailAccounts.objects.filter(e_id=k)
            para={'username':a.username,'pr':a.provider,'email':a.email,'name':name,'account':True,'e':e,'id':a.id,'default':acdetail.defaultaccount,'form':form}
        else:
            para={'username':a.username,'email':a.email,'pr':a.provider,'name':name,'account':False,'id':a.id,'default':acdetail.defaultaccount,'form':form}

        if check=="account":
            return render(request,'emailaccount/addemail.html',para)
        else:
            return render(request,'emailaccount/addemail.html',para)
    else:
        return redirect('accounting:login')
def contact(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        check=check_database(k)
        if check is not None:
            return redirect('accounting:complete_test')
        else:
            form=FileUploadForm()
            a=Account.objects.get(pk=k)
            n=a.name
            name=n.split(' ')
            name=name[0]
            if Contactlist.objects.filter(c_id=k).exists():
                c=Contactlist.objects.filter(c_id=k)
                para={'username':a.username,'email':a.email,'name':name,'id':a.id,'form':form,'c':c}
            else:
                para={'username':a.username,'email':a.email,'name':name,'id':a.id,'form':form}
            return render(request,'emailaccount/contact.html',para)
    else:
        return redirect('accounting:login')
def mailbox(request):
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
            print(para)
            return render(request,'emailaccount/mailbox.html',para)
    else:
        return redirect('accounting:login')
def contactfile(request):
    type=request.POST.get('type')
    if type=='start' and request.FILES['myfile']:
        id=request.POST.get('id')
        ids=int(id)
        a=Account.objects.get(pk=ids)
        contactlistfile=ContactlistFile()
        contactlistfile.cf_id=a
        photo=request.FILES['myfile']
        print(photo)
        a.contactlistfile_set.create(myfile=photo,date=datetime.now())
        return redirect('emailaccount:contact')

    else:
        return HttpResponse("Invalid Url")
#Upload User Photo
def userphoto(request):
    type=request.POST.get('type')
    if type=="start":
        id=request.POST.get('id')
        a=Accountdetail.objects.get(acc_id=id)
        a.profile=request.FILES['profile']
        a.save()
        return redirect('emailaccount:accountsetting')
    else:
        return HttpResponse("Wrong Url")
###ADD EMAILSS
def addemail(request):
    type=request.POST.get('type')
    if type=="start":
        id=request.POST.get('id')
        ids=int(id)
        provider=request.POST.get('provider')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if EmailAccounts.objects.filter(e_id=ids,e_email=email).exists():
            data={
                'is_have':"done"
            }
            return JsonResponse(data)
        encode=password.encode()
        encoded_text =Cipher_suites.encrypt(b"%s"%(encode))
        encoded_password=encoded_text.decode("utf-8")
        a=Account.objects.get(pk=ids)
        emailaccounts=EmailAccounts()
        emailaccounts.e_id=a
        a.emailaccounts_set.create(e_provider=provider,e_email=email,e_password=encoded_password,addon=datetime.now())
        data={
            'is_created':"n"
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Wrong Url")
def changename(request):
    type=request.POST.get('type')
    if type=="start":
        id=request.POST.get('id')
        name=request.POST.get('name')
        a=Account.objects.get(pk=id)
        a.name=name
        a.save()
        data={
            'is_change':'chnage'

        }
        return JsonResponse(data)
    else:
        return HttpResponse("wrong")
def chnageemailpassword(request):
    type=request.POST.get('type')
    if type=="start":
        email=request.POST.get('email')
        id=request.POST.get('id')
        passw=request.POST.get('password')
        ol=request.POST.get('old')
        e=EmailAccounts.objects.get(e_id=id,e_email=email)
        email_pass=e.e_password
        decoded=email_pass.encode()
        decoded_pass=Cipher_suites.decrypt(decoded)
        decoded_text=decoded_pass.decode()
        print(decoded_text,ol,passw)
        if ol!=decoded_text:
            data={
                'is_done':'false'
            }
            return JsonResponse(data)
        encode=passw.encode()
        encoded_text =Cipher_suites.encrypt(b"%s"%(encode))
        encoded_password=encoded_text.decode("utf-8")
        e.e_password=encoded_password
        print(encoded_password)
        e.save()
        data={
            'ok':'ok'
        }
        return JsonResponse(data)
    else:
        return HttpResponse("wrong url")
#####Make default ACCOUNT

def makedefault(request):
    type=request.POST.get('type')
    if type=="start":
        id=request.POST.get('butt')
        e=EmailAccounts.objects.get(id=id)
        id=e.e_id
        a=Accountdetail.objects.get(acc_id=id)
        a.defaultaccount=e.e_email
        a.save()
        data={
            'is_default':'delete'
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Wrong Url")

def remove(request):
    type=request.POST.get('type')
    if type=="start":
        id=request.POST.get('button')
        e=EmailAccounts.objects.filter(pk=id)
        if email.e_email==account_detail.defaultaccount:
            account_detail.defaultaccount=None
            account_detail.save()
        e.delete()
        data={
            'is_delete':'de'
        }
        return JsonResponse(data)
    else:
        return HttpResponse("Wrong Url")
def chnageaccpassword(request):
    if not request.session.session_key:
        request.session.save()
    s=request.session._session_key
    k=findkey(s)
    if k is not None:
        a=Account.objects.get(pk=k)
        para={'id':a.id}

        return render(request,'emailaccount/accountpassword.html',para)
    else:
        return redirect('accounting:login')

def verifychnagepassword(request):
    type=request.POST.get('type')
    if type=="start":
        old=request.POST.get('old')
        passw=request.POST.get('password')
        id=request.POST.get('id')
        print(id,old,passw)
        a=Account.objects.get(pk=id)
        acc=Account.objects.filter(pk=id)
        password=a.password
        check=check_password(old,password)
        print(check)
        if check is True:
            passwor=make_password(passw)
            acc.update(password=passwor)
            data={
                'is_done':'done'
            }

            if Session.objects.filter(createid=id).exists():
                s=Session.objects.filter(createid=id)
                s.delete()
            return JsonResponse(data)
        else:
            print(check)
            data={
                'is_wrong':'wrong'
            }
            return JsonResponse(data)

    else:
        return HttpResponse('Wrong Url')
def addcontacts(request):
    type=request.POST.get('type')
    if type=="start":
        id=request.POST.get('id')
        name=request.POST.get('name')
        fname=request.POST.get('firstname')
        mname=request.POST.get('middlename')
        lname=request.POST.get('lastname')
        group=request.POST.get('group')
        subgroup=request.POST.get('subgroup')
        status=request.POST.get('status')
        company=request.POST.get('company')
        deignation=request.POST.get('deignation')
        gender=request.POST.get('gender')
        title=request.POST.get('title')
        depart=request.POST.get('department')
        uni=request.POST.get('university')
        degree=request.POST.get('degree')
        py=request.POST.get('passingyear')
        college=request.POST.get('college')
        ctc=request.POST.get('ctc')
        email=request.POST.get('emailid')
        aemailid=request.POST.get('alternateemailid')
        phone=request.POST.get('phone')
        aphone=request.POST.get('alternatephone')
        city=request.POST.get('city')
        add=request.POST.get('address')
        state=request.POST.get('state')
        country=request.POST.get('country')
        zip=request.POST.get('zip')
        industry=request.POST.get('industry')
        keyskills=request.POST.get('keyskills')
        tex=request.POST.get('totalexperience')
        yob=request.POST.get('yearinbusiness')
        turnover=request.POST.get('turnover')
        doi=request.POST.get('dateofincorporation')
        emp=request.POST.get('employees')
        if Contactlist.objects.filter(c_id=id,c_email=email).exists():
            a=Account.objects.get(pk=id)
            n=a.name
            name=n.split(' ')
            name=name[0]
            form=FileUploadForm()
            para={'username':a.username,'email':a.email,'name':name,'id':a.id,'form':form,'error':'alreadyexists'}
            return render(request,'emailaccount/contact.html',para)
        else:
            a=Account.objects.get(pk=id)
            contactlist=Contactlist()
            contactlist.c_id=a
            a.contactlist_set.create(c_name=name,c_first_name=fname,c_middle_name=mname,c_last_name=lname,c_group=group,c_gender=gender,c_subgroup=subgroup,c_status=status,
                                     c_company=company,c_designation=deignation,c_title=title,c_department=depart,c_university=uni,c_degree=degree,c_passingyear=py,
                                     c_college=college,c_ctc=ctc,c_email=email,c_alternativeemailid=aemailid,c_phone=phone,c_alternativephone=aphone,c_city=city,c_address=add,
                                     c_state=state,c_country=country,c_zip=zip,c_industry=industry,c_keyskills=keyskills,c_totalexperience=tex,c_yearbusiness=yob,c_turnover=turnover,
                                     c_dateofincorportaion=doi,c_employess=emp,c_addon=datetime.now())
            return redirect('emailaccount:contact')

    else:
        return HttpResponse("Wrong Url")
def groups(request):
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
            para={'username':a.username,'email':a.email,'name':name,'id':a.id}
            return render(request,'emailaccount/groups.html',para)
    else:
        return redirect('accounting:login')
