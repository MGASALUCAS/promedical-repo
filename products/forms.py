from django.forms import ModelForm
from .models import Customer, Doctor


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class PrivateDoctor(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
