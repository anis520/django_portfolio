from django import forms



class FormData(forms.Form):
         name=forms.CharField(error_messages={'required':'not allowed'})
         email=forms.EmailField()
         text=forms.CharField(widget=forms.Textarea(attrs={"rows":"2"}),label='Text your comment',) 
           