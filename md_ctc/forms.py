from django.contrib.auth.models import User
from md_ctc.models import Scan
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ScanForm(forms.ModelForm):
    class Meta:
        model = Scan
        fields = ('ct_scan', 'cancer',)
