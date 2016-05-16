from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.core.mail import EmailMessage
#from django.core.mail import send_mail


# Create your views here.

def index(request):
    context_dict = {}

    return render(request, 'landing/index.html', context_dict)

def contact(request):
    data = {}

    if request.method == 'POST':


        data["result"] = "Data arrived on the server!"

        if request.is_ajax():
            data["success"] = True
            return JsonResponse(data)
        else:
            data["success"] = False
            return JsonResponse(data)
    return render(request, 'landing/index.html', data)
