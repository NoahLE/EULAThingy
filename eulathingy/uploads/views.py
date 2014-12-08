from django.http.response import HttpResponse
from django.shortcuts import render
from uuid import uuid4
from django.conf import settings


def upload(request):
        return render(request, 'uploads/upload.html')


def upload_nginx(request):
    uploaded_file = request.FILES['upload_file']
    filename, path = _handle_file(uploaded_file)
    

    return HttpResponse(str(request.FILES))

def _handle_file(f):
    identifier = str(uuid4())
    path = settings.FILE_LOCATION
    full_path = '{}/{}'.format(path, identifier)

    with open(full_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return identifier, path