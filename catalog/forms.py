from datetime import date, datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from work import settings


class ModeDate(forms.Form):
    q=forms.CharField(max_length=20,label='Точка отправления')
    a=forms.CharField(max_length=20,label='Точка приезда')
    t = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,label='Дата отправления')
class SignUp(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username',
                'first_name',
                'last_name',
                'email' ,
                'password1',
                'password2' )

class EditForm(UserChangeForm):

    class Meta:
        model = User
        fields=('first_name',
                'last_name',
                'email'
                )

