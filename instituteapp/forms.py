from django import forms
from django.contrib.auth.models import User
from .models import CommentData


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text Here...', 'cols':10, 'rows':10}))
    class Meta:
        model = CommentData
        fields = ('content',)



class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label='Enter FirstName', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'FirstName'}))
    last_name = forms.CharField(label='Enter lastName', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'lastName'}))
    username= forms.CharField(label='Enter UserName', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder':'UserName'}))
    email = forms.EmailField(label='Enter Email', widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    password = forms.CharField(label='Enter Password', widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))






    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')



class ContactForm(forms.Form):
    first_name = forms.CharField(
        label = 'Enter First Name',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'First Name...'
            }
        )
    )
    last_name = forms.CharField(
        label = 'Enter Last Name',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Last Name...'
            }
        )
    )
    email = forms.EmailField(
        label = 'Enter Email',
        widget = forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Email...'
            }
        )
    )
    mobile = forms.IntegerField(
        label = 'Enter Mobile Number',
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Number...'
            }
        )
    )
    location = forms.CharField(
        label = 'Enter Location',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Your Location...'
            }
        )
    )
    courses = forms.CharField(
        label = 'Enter Courses',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Courses Name...'
            }
        )
    )
    referred_by = forms.CharField(
        label = 'Enter Name',
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Referred Person Name...'
            }
        )
    )


