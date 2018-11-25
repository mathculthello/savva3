from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib import messages
from django.core.mail import mail_managers

from .models import Event


from .forms import InviteForm

from .models import Event
# Create your views here.

def invite(request):
	success = False
	if request.method == 'POST':
		formset = InviteForm(request.POST)
		if formset.is_valid():
			formset.save()
			messages.success(request, 'Ваше приглашение отправлено')
			success = True
			formset = None
			mail_managers("Invite",'check admin')
		else:
			fromset = formset
		context = {
		'formset':formset,
		'success':success
		}
	else: 
		formset = InviteForm
		context = {
		'formset': formset
		}

	return render(request, 'events/invite.html', context)


def archive(request):
    events=Event.objects.all()
    context={'events':events}
    return render(request, 'events/archive.html', context)

def events(request):
    events=Event.future.all()
    context={'events':events}
    return render(request, 'events/events.html',context)

def event(request, event_id):
    event=Event.objects.get(id=event_id)
    context={
    'event':event,
    'meta':event.as_meta(),
    }
    return render(request, 'events/event.html', context)
