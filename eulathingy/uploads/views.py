from uuid import uuid4
from django.db import transaction

from django.db.models.loading import get_model
from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings

from parsers import procedures


ThingyDoc = get_model('thingys', 'ThingyDoc')


def upload(request):
    return render(request, 'uploads/upload.html')


def upload_nginx(request):
    uploaded_file = request.FILES['upload_file']
    filename, path = _handle_file(uploaded_file)
    doc = ThingyDoc(
        title=request.POST.get('title', 'We will never know :-('),
    )
    doc.save()
    with transaction.commit_on_success():
        strings = procedures.generate_strings(path, filename, doc)
        for string in strings:
            string.save()

    return HttpResponse(str(request.FILES))


def _handle_file(f):
    identifier = str(uuid4())
    path = settings.FILE_LOCATION
    full_path = '{}/{}'.format(path, identifier)

    with open(full_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return identifier, path