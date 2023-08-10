from django import forms
from .models import Notifications


class NotificationsAddForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = "__all__"