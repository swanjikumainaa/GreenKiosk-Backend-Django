from django import forms
from .models import Discounts


class DiscountUploadForm(forms.ModelForm):
    class Meta:
        model = Discounts
        fields = "__all__"

