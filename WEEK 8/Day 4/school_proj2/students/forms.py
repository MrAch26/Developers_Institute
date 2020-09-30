from django import forms

class AddStudentForm(forms.Form):
      first_name = forms.CharField(required=True)
      last_name = forms.CharField(required=True)

      major = forms.CharField(required=False)
      minor = forms.CharField(required=False)
      picture = forms.URLField(required=False,label="Pic URL")

