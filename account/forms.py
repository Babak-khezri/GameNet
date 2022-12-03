from csv import field_size_limit
from django import forms
from .models import User


class UserForm(forms.ModelForm):

    

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','salary', 'username', 'password']