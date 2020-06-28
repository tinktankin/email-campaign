from datetime import date
from django.db.models.signals import post_save

from django.utils.timezone import datetime
from djongo import models

def user_directory_path(instance,filename):
    return 'contactlist/{folder}/{date}/{file}'.format(id=instance,folder=instance.cf_id,date=date.today(),file=filename)
def user_photo_path(instance,filename):
    return 'photo/{folder}/{date}/{file}'.format(id=instance,folder=instance.acc_id,date=date.today(),file=filename)

class Account(models.Model):
    provider=models.CharField(max_length=40,null=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30,unique=True)
    username=models.CharField(max_length=100,null=True,unique=True)
    token_id=models.CharField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    created_on=models.DateTimeField(default=datetime.now())

class Accountdetail(models.Model):
    acc_id=models.OneToOneField(Account,on_delete=models.CASCADE)
    city=models.CharField(max_length=100,null=True)
    potp=models.CharField(max_length=200,null=True)
    rotp=models.CharField(max_length=200,null=True)
    date2=models.DateTimeField(default=datetime.now())
    date=models.DateTimeField(default=datetime.now())
    defaultaccount=models.EmailField(null=True)
    profile=models.ImageField(upload_to=user_photo_path,null=True)
    everify=models.BooleanField(default=False)
    comlpeted=models.BooleanField(default=False)
    def update_account(sender,**kwargs):
        Accountdetail.objects.create(acc_id=kwargs['instance'])
    post_save.connect(update_account,sender=Account)

class EmailAccounts(models.Model):
    e_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    e_provider=models.CharField(max_length=50)
    e_email=models.EmailField()
    e_password=models.CharField(max_length=200)
    addon=models.DateTimeField(default=datetime.now())
    addpassword=models.BooleanField(default=False)

class Contactlist(models.Model):
    c_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    c_name=models.CharField(max_length=50)
    c_first_name=models.CharField(max_length=50,default=None)
    c_middle_name=models.CharField(max_length=50,default=None)
    c_last_name=models.CharField(max_length=50,default=None)
    c_gender=models.CharField(max_length=40,default=None)
    c_group=models.CharField(max_length=50,default=None)
    c_subgroup=models.CharField(max_length=50,default=None)
    c_status=models.CharField(max_length=50,default=None)
    c_company=models.CharField(max_length=50,default=None)
    c_designation=models.CharField(max_length=50,default=None)
    c_title=models.CharField(max_length=50,default=None)
    c_department=models.CharField(max_length=50,default=None)
    c_university=models.CharField(max_length=50,default=None)
    c_degree=models.CharField(max_length=50,default=None)
    c_passingyear=models.CharField(max_length=50,default=None)
    c_college=models.CharField(max_length=50,default=None)
    c_ctc=models.CharField(max_length=50,default=None)
    c_email=models.EmailField()
    c_alternativeemailid=models.EmailField(default=None)
    c_phone=models.CharField(max_length=40,default=None)
    c_alternativephone=models.CharField(max_length=40,default=None)
    c_city=models.CharField(max_length=50,default=None)
    c_address=models.CharField(max_length=50,default=None)
    c_state=models.CharField(max_length=50,default=None)
    c_country=models.CharField(max_length=50,default=None)
    c_zip=models.CharField(max_length=50,default=None)
    c_industry=models.CharField(max_length=50,default=None)
    c_keyskills=models.CharField(max_length=50,default=None)
    c_totalexperience=models.CharField(max_length=50,default=None)
    c_yearbusiness=models.CharField(max_length=50,default=None)
    c_turnover=models.CharField(max_length=50,default=None)
    c_dateofincorportaion=models.CharField(max_length=50,default=None)
    c_employess=models.CharField(max_length=50,default=None)
    c_addon=models.DateTimeField(default=datetime.now())

class ContactlistFile(models.Model):
    cf_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now())
    myfile=models.FileField(upload_to=user_directory_path)

class Group(models.Model):
    g_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    g_name=models.CharField(max_length=30,default=None)
    add_on=models.DateTimeField(default=datetime.now())

class Groupdetails(models.Model):
    gd_id=models.ForeignKey(Group,on_delete=models.CASCADE)
    contact_id=models.IntegerField(default=0)

class Campaigns(models.Model):
    ca_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    ca_name=models.CharField(max_length=30)
    add_on=models.DateTimeField(default=datetime.now())

class Campaignsdetails(models.Model):
    cd_id=models.ForeignKey(Campaigns,on_delete=models.CASCADE)
    contact_id=models.IntegerField(default=0)

class Stats(models.Model):
    s_id=models.ForeignKey(Account,on_delete=models.CASCADE)
    From=models.DateTimeField(default=datetime.now())
    To=models.DateTimeField(default=datetime.now())
    messagesent=models.IntegerField(default=0)
    contacts_created=models.IntegerField(default=0)
    groups_created=models.IntegerField(default=0)
    campaigns_created=models.IntegerField(default=0)
    templated_created=models.IntegerField(default=0)

class Session(models.Model):
    createid=models.CharField(max_length=100)
    session_id=models.CharField(max_length=300)
    session_key=models.CharField(max_length=100)
