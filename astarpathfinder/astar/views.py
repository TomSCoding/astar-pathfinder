from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</body></html></h1>" % now
    return HttpResponse(html)