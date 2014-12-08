from django.db.models.aggregates import Sum
from django.shortcuts import render, render_to_response, redirect
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
    context = RequestContext(request)
    docid = int(request.path.split('/')[-1:][0])
    doc = ThingysDoc.objects.get(pk=docid)
    strings = ThingysString.objects.filter(doc=doc)
    context_dict = {
        'doc': doc,
        'strings': strings
    }

    return render_to_response('dashboard/read.html', context_dict, context)


def results(request):
    context = RequestContext(request)
    docs = ThingysDoc.objects.order_by('-rating')[:20]
    context_dict = {'docs': docs}

    return render_to_response('dashboard/results.html', context_dict, context)


def app(request):

    if request.method == 'GET':
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
    elif request.method == 'POST':

        selected = request.POST.items()[0][0]
        if selected == 'critical':
            incr = 2
        elif selected == 'noteworthy':
            incr = 1
        else:
            incr = 0

        thingyid = int(request.path.split('/')[-1:][0])
        thingy_string = ThingysString.objects.get(pk=thingyid)

        thingy_string.rating += incr
        thingy_string.save()

        thingy_doc = thingy_string.doc
        thingy_doc.rating = ThingysString.objects.filter(
            doc=thingy_doc
        ).aggregate(Sum('rating'))['rating__sum']
        thingy_doc.save()
        return redirect('/dashboard/app')

