from django import forms
from .models import Payment


class MakePaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"