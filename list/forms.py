from django import forms
from .models import list_krsteni

class list_krsteniForm(forms.ModelForm):
    class Meta:
        model = list_krsteni
        fields = ['knjiga', 'strana']