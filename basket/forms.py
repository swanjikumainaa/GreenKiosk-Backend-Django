from django import forms
from .models import Shopping_cart


class CartAddForm(forms.ModelForm):
    class Meta:
        model = Shopping_cart
        fields = "__all__"