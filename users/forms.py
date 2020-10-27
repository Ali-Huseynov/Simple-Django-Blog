from django.contrib.auth.forms import UserCreationForm ,  UserChangeForm
from .models import Profile
from django import forms
from django.contrib.auth.models import User


class CreateUserForm( UserCreationForm ):
    class Meta:
        model = User

        fields = [ 'username' ,'first_name', 'last_name', 'password1', 'password2' ]

class UpdateUserForm( forms.ModelForm  ):
    class Meta:
        model = User
        fields = ['first_name', 'last_name' ]


class UpdateProfileForm( forms.ModelForm ):
    class Meta:
        model = Profile

        fields = [ 'pic' , 'about'  ]




