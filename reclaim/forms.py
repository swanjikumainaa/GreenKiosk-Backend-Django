from django import forms
from .models import Account_recovery


class RecoverAccountForm(forms.ModelForm):
    class Meta:
        model = Account_recovery
        fields = "__all__"