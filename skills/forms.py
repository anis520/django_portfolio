from django import forms


class Data_form(forms.Form):
    Name=forms.CharField()
    Email=forms.EmailField() 