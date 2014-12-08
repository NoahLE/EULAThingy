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

def app(request):
    context = RequestContext(request)

    # find least voted on document
    sad_doc = ThingysString.objects.order_by('string_rating')
    # sort by least voted on strings
    # sad_doc = sad_doc.objects.order_by('rating')  # foreign key
    # pick bottom string and two surrounding strings

    # send as output


    primary_string = 'You also agree that you will not use these products for any purposes prohibited by United States law, including, without limitation, the development, design, manufacture or production of nuclear, missiles, or chemical or biological weapons.'

    context_dict = {'primary_string': primary_string}

    return render_to_response('dashboard/app.html', context_dict, context)

