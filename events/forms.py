from .models import Invite
from django.forms import ModelForm

class InviteForm(ModelForm):
	class Meta:
		model=Invite
		exclude = ['date']
