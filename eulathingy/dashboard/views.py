from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
    return render(request, 'dashboard/index.html')

def contact(request):
    return render(request, 'dashboard/contact.html')

def app(request):
    context = RequestContext(request)

    primary_string = 'You also agree that you will not use these products for any purposes prohibited by United States law, including, without limitation, the development, design, manufacture or production of nuclear, missiles, or chemical or biological weapons.'
    context_string1 = 'By using the Licensed Application, you represent and warrant that you are not located in any such country or on any such list.'
    context_string2 = 'h. The Licensed Application and related documentation are "Commercial Items", as that term is defined at 48 C.F.R. 2.101, consisting of "Commercial Computer Software" and "Commercial Computer Software Documentation", as such terms are used in 48 C.F.R. 12.212 or 48 C.F.R. 227.7202, as applicable.'

    context_dict = {}
    context_dict['primary_string'] = primary_string
    context_dict['context_string1'] = context_string1
    context_dict['context_string2'] = context_string2


    return render_to_response('dashboard/app.html', context_dict, context)
