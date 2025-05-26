from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=11)
    age = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'age', 'password1', 'password2']
