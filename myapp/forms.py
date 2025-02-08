from django import forms
from .models import media

class imgForm(forms.ModelForm):
    class Meta:
        model = media
        fields='__all__'
        # fields = {'name','image','price','description'}

        # widgets = {
        #     'name':forms.TextInput(attrs={'class': 'form-control'}),
        #     'image':forms.FileInput(attrs={'class': 'form-control'}),
        #     'price':forms.TextInput(attrs={'class': 'form-control'}),  
        #     'description':forms.TextInput(attrs={'class': 'form-control'})
        # }