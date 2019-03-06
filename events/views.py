from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib import messages
from django.core.mail import send_mail

from .models import Event


from .forms import InviteForm

from .models import Event
# Create your views here.

def invite(request):
	success = False
	if request.method == 'POST':
		formset = InviteForm(request.POST)
		if formset.is_valid():
			model=formset.save()
			messages.success(request, 'Ваше приглашение отправлено')
			success = True
			formset = None
			send_mail("Приглашение." + model.city,
                        model.theme + '\n' +
                        model.name + '\n' +
                        model.email + '\n' +
                        model.phone + '\n' +
                        model.comment,
						'django@savvateev.xyz',
						['savvaorg@googlegroups.com']
                        )
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

def google_calendar(request):
	return render(request, 'events/google_calendar.html')

def events(request):
    # Переадресуем на вики
    return redirect('https://wiki.savvateev.xyz/doku.php?id=лекции')
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
