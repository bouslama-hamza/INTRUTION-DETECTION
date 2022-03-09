from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView

#class for the login
class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'hi'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "password"]:
            self.fields[fieldname].help_text = None
        
    class Meta:
        model = User
        fields = ("username" , "password")

class UserUpdateForm(UserCreationForm):

    username = forms.CharField(max_length=30 , label= "" , widget=forms.TextInput({'placeholder':'Username'}))
    first_name = forms.CharField(max_length=10 , label= "" , widget=forms.TextInput({'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=10 , label= "" , widget=forms.TextInput({'placeholder':'Last Name'}))
    email = forms.EmailField(label= "" , widget=forms.EmailInput({'placeholder':'Email Adrress'}))
    password1 = forms.CharField(label="",widget=forms.PasswordInput({'placeholder':'New Password'}))
    password2 = forms.CharField(label="",widget=forms.PasswordInput({'placeholder':'Confirme New Password'}))

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "first_name" ,"last_name" , "email", "password1", "password2" ]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username" ,"first_name" ,"last_name" , "email", "password1", "password2")

# class for the reset
class ResetPassword(PasswordResetView):
    
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email', 'id': 'hello'}))

    def __init__(self, *args, **kwargs):
        super(ResetPassword, self).__init__(*args, **kwargs)

        for fieldname in ["email"]:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("email")

