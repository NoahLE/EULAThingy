from uuid import uuid4
from django.db import transaction

from django.db.models.loading import get_model
from django.shortcuts import render, redirect
from django.conf import settings

from parsers import procedures

import os


ThingyDoc = get_model('thingys', 'ThingyDoc')


def upload(request):
    return render(request, 'uploads/upload.html')


@transaction.atomic
def upload_nginx(request):
    uploaded_file = request.FILES['upload_file']
    filename, path = _handle_file(uploaded_file)
    try:
        doc = ThingyDoc(
            title=request.POST.get('title', 'We will never know :-('),
        )
        doc.save()
        strings = procedures.generate_strings(path, filename, doc)
        for string in strings:
            string.save()
    finally:
        os.remove(path + '/' + filename)

    return redirect('/dashboard/app')


def _handle_file(f):
    identifier = str(uuid4())
    path = settings.FILE_LOCATION
    full_path = '{}/{}'.format(path, identifier)

    with open(full_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return identifier, path