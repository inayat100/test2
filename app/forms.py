from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user_details,Post
from django import forms

class detail_form(forms.ModelForm):
    class Meta:
        model = user_details
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'choice': forms.Select(attrs=({'class': 'form-select '})),
            'image': forms.FileInput(attrs=({'class': 'form-control'})),
            'address': forms.Textarea(attrs=({'class': 'form-control'})),
        }

class user_form(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2'}),
                                help_text=('make a strong password'))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2'}),
        help_text=('make a strong password'))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs=({'class': 'form-control'})),
            'first_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'last_name': forms.TextInput(attrs=({'class': 'form-control'})),
            'email': forms.EmailInput(attrs=({'class': 'form-control'})),

        }

class singin_form(forms.Form):
    User_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-2','placeholder':'Enter Your Username Here'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2','placeholder':'Enter Your Password Here'}))

class post_form(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'title': forms.TextInput(attrs=({'class': 'form-control '})),
            'image': forms.FileInput(attrs=({'class': 'form-control'})),
            'category': forms.Select(attrs=({'class': 'form-control'})),
            'summary': forms.TextInput(attrs=({'class':'form-control'})),
            'content': forms.Textarea(attrs=({'class': 'form-control'})),
            'Publish': forms.CheckboxInput(attrs=({'class': 'form-check-input'})),
        }
