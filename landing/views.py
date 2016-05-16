from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):
    context_dict = {}

    return render(request, 'landing/index.html', context_dict)
