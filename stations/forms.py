from django import forms

class StationForm(forms.Form):
    zip_code = forms.CharField(label='Zip Code', max_length=5)
    miles = forms.IntegerField(label='Miles')