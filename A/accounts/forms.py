from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Your Username'}))

    password = forms.CharField(max_length=30, required=True,widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Your Password'}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Your Username'}))

    email = forms.EmailField(max_length=50,widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':'Your Email'}))

    password = forms.CharField(label='Password', max_length=30, required=True,widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Your Password'}))

    repassword = forms.CharField(label='Repassword', max_length=30, required=True,widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'Your Repassword'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('email already exists')
        return email

    def clean_repassword(self):
        pass1 = self.cleaned_data['password']
        repass = self.cleaned_data['repassword']
        if pass1 != repass:
            raise forms.ValidationError('passwoed not match repassword')
        return pass1
