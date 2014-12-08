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


def read(request):
    return render(request, 'dashboard/read.html')


def results(request):
    context = RequestContext(request)
    docs = ThingysDoc.objects.order_by('-rating')[:20]
    context_dict = {'docs': docs}

    return render_to_response('dashboard/results.html', context_dict, context)


def app(request):
    context = RequestContext(request)

    # find least voted on document
    qs = ThingysString.objects.order_by('last_updated')[:1]
    if qs:
        single_string = qs[0]
        context_dict = {
            'title': single_string.doc.title,
            'category': single_string.doc.get_category_display(),
            'primary_string': single_string.string,
            'string_id': single_string.id
        }
    else:
        context_dict = {}

    return render_to_response('dashboard/app.html', context_dict, context)

