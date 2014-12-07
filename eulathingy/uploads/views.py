from django.http.response import HttpResponse
from django.shortcuts import render


def upload(request):
        return render(request, 'uploads/upload.html')


def upload_nginx(request):
    return HttpResponse(str(request.POST))