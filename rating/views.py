from django.shortcuts import render
from django.http import HttpResponseBadRequest, Http404, JsonResponse
from django.views.decorators.http import require_http_methods
from django.apps import apps
from rating.models import Rating
import json

def is_already_voted(rating_type, ip, iid):
    try:
        Rating.objects.get(
            rating_type=rating_type,
            ip=ip,
            iid=iid
        )

        return True
    except Rating.DoesNotExist:
        return False

def get_rating_model(rating_type):
    app_label, model_name = rating_type.split('.')
    return apps.get_model(
        app_label=app_label, 
        model_name=model_name
    )

def parse_request(request):
    body = json.loads(request.body)
    rating_type = body.get('rating_type', '')
    iid = body.get('iid', 0)
    value = body['value']
    ip = request.META['REMOTE_ADDR']

    if value > 1 or value < -1 or value == 0:
        return HttpResponseBadRequest(json.dumps({
            "message": "INVALID_VALUE"
        }))

    return (rating_type, iid, value, ip)

@require_http_methods(["POST"])
def update(request):
    rating_type, iid, value, ip = parse_request(request)

    if is_already_voted(rating_type, ip, iid):
        return HttpResponseBadRequest(json.dumps({
            "message": "ALREADY_VOTED"
        }))
    Model = get_rating_model(rating_type)
    model = Model.objects.get(pk=iid)
    model.update_rating(value)
    Rating.create(
        rating_type=rating_type,
        iid=iid,
        ip=ip,
        value=value
    )

    return JsonResponse({
        "rating": model.rating
    })
     