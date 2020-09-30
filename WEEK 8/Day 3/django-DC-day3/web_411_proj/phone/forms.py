from django import forms
from phonenumber_field.formfields import PhoneNumberField


class SearchForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100, required=False)
    phone_number = PhoneNumberField(required=False)
