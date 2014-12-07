from django.shortcuts import render
from django.template import RequestContext


# Create your views here.
def index(request):
    context = RequestContext(request)



    return render(request, 'dashboard/index.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def app(request):
    return render(request, 'dashboard/app.html')

def upload(request):
    return render(request, 'dashboard/upload.html')