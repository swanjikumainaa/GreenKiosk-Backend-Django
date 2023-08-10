from django import forms
from .models import Order


class OrderPlacementForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"