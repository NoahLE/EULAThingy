from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def app(request):
    return render(request, 'dashboard/app.html')