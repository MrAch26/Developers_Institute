from django import forms

# def validate_major(major):
#     # check if they are numbers in the name
#     if major != "Computer Programming":
#         print("Invalid Major")  
#         raise forms.ValidationError(f'This is a bootcamp. Your major must be Computer Programming')


class AddStudentForm(forms.Form):

      def sayHi(self):
            print("HI, I'm a studentForm for adding new students.")

      # def __init__(self, *args, **kwargs):
      #       super(AddStudentForm, self).__init__(*args, **kwargs)
      #       for item in self.visible_fields():
      #             item.field.widget.attrs['class'] = 'form-control'

      first_name = forms.CharField(
            required=True,
            label="Given Name", 
            help_text='This is the name your Momma gave you', 
            error_messages={'required': 'We need to know how to call'}
      )

      last_name = forms.CharField(
            required = True,
            widget = forms.TextInput(
                  attrs={
                        'placeholder': 'Write your name here',
                        'class': 'form-control'
                  }
            )
      )

      major = forms.CharField(
            required=False,
            # validators = [validate_major]
      )

      minor = forms.CharField(required=False, widget = forms.TextInput(attrs={'class': 'form-control'}))

      picture = forms.URLField(required=False,label="Pic URL", widget = forms.TextInput(attrs={'class': 'form-control'}))