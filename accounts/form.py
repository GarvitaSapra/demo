from django.forms import ModelForm
from .models import order, Customer
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class OrderForm(ModelForm):
    class Meta:
        model = order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=commit)
        Customer.objects.create(user=user)
        return user