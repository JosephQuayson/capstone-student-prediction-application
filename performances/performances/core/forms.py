from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from . models import performancePredict


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PredictModel(ModelForm):
    class Meta:
        model = performancePredict
        fields='__all__'
        exclude = ['classification']
