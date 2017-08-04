from django import forms

class PeopleCreateForm(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    age = forms.IntegerField(required=False)
