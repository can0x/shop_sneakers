from django.forms import ModelForm
from .models import CartItem, User, Order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from flask import request


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = '__all__'
