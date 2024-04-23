from django import forms
from .models import services
class EditServicesForm(forms.ModelForm):
    service_name = forms.CharField(max_length=255)
    service_description = forms.Textarea()
    service_price = forms.FloatField()
    service_qty = forms.IntegerField()
    class Meta:
            model = services
            fields = ['service_name', 'service_description', 'service_price', 'service_qty']
    labels = {
        "service_name":  "Service Name",
        "service_description": "Service Description",
        "service_price": "Service Price",
        "service_qty": "Service qty",
    }
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)