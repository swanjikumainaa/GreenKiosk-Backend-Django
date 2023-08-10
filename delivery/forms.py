from django import forms
from .models import Shipment


class DispatchShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = "__all__"