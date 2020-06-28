from django import forms
from accounting.models import ContactlistFile,Accountdetail

class FileUploadForm(forms.ModelForm):
    class Meta:
        model=ContactlistFile
        fields=('myfile',)
class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model=Accountdetail
        fields=('profile',)
