from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.db.models.loading import get_model

ThingysString = get_model(
    'thingys',
    'ThingyString'
)

ThingysDoc = get_model(
    'thingys',
    'ThingyDoc'
)


def index(request):
    return render(request, 'dashboard/index.html')


def contact(request):
    return render(request, 'dashboard/contact.html')

def results(request):
    return render(request, 'dashboard/results.html')

def app(request):
    context = RequestContext(request)

    # find least voted on document
    qs = ThingysString.objects.order_by('-rating')[:1]

    if qs:
        single_string = qs[0]
        context_dict = {
            'primary_string': single_string.string,
            'string_id': single_string.id
        }
    else:
        context_dict = {}

    return render_to_response('dashboard/app.html', context_dict, context)

