from django.shortcuts import render


def upload(request):
    method = request.method

    if method == 'GET':
        return render(request, 'uploads/upload.html')
    elif method == 'POST':
        import ipdb; ipdb.set_trace()
        file = request.FILES[0]
        content = file.read()
