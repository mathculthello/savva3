from django.forms import ModelForm, Textarea
from .models import Formulae

class FormulaeForm(ModelForm):
    class Meta:
        model=Formulae
        fields=['formulae']
        labels={
        'formulae': ''
        }
