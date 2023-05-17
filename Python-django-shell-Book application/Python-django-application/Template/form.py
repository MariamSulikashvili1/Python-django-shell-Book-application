from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_lastname = forms.CharField(label='Your lastname', max_length=100)



