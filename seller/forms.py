from django import forms
from .models import Vendor


class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = "__all__"



