from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select
from patient_app.models import UserInfo
from django.contrib.auth.forms import UserCreationForm  

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ("name", "age", "sex", "location","health")
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'age': NumberInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'age'
                }),
            'sex': Select(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'sex'
                }),
            'location': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'location'
                }),
            'health': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'existing health conditions'
                }),                                 
        }


class Question(forms.Form):
    question = forms.CharField(max_length=500)