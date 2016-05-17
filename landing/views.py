from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError


# Create your views here.

def index(request):
    context_dict = {}

    return render(request, 'landing/index.html', context_dict)

def contact(request):
    context_dict = {}

    if request.method == 'POST':
        subject = "Message from exclave solutions site"
        message = request.POST.get("message")
        from_email = request.POST.get("email","")

        if subject and message and from_email:
            try:
                context_dict["succes"] = True
                send_mail(subject,message,from_email,['festus.yeboah@hotmail.com'])
            except BadHeaderError:
                context_dict["succes"] = False
                return render(request, 'landing/index.html', context_dict)
            return render(request, 'landing/index.html', context_dict)
        else:
            return render(request, 'landing/index.html', context_dict)
