from django import forms
from django.core.validators import EmailValidator


class suggestForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Movie/Series Name', 'class': 'form-control'}))
    rating = forms.DecimalField( max_value=10, min_value=0, widget=forms.NumberInput(attrs={'step': "0.1", 'class': 'form-control'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'placeholder': 'Short Description!', 'class': 'form-control'}))
    type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Movie/Series', 'class': 'form-control'}))



class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.CharField(validators=[EmailValidator()], widget= forms.EmailInput(attrs={'placeholder': 'abc@xyz.com', 'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message!', 'class': 'form-control'}))
    