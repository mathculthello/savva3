from django.forms import ModelForm, Textarea
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=['theme','text','author','email']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 5}),
        }
