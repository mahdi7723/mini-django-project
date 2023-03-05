from django import forms

from uploadapp.models import Uploads, UploadFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = '__all__'


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = '__all__'
