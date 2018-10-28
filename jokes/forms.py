from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from django.urls import reverse


from .models import Joke

class JokeForm(ModelForm):
    class Meta:
        model=Joke
        fields=['title','text','author']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 6}),
        }
