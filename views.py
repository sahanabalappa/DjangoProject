from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):

	if request.method=="POST":
		return HttpResponse("Hello World!, POST")
	else:
		return HttpResponse("Hello World!, GET")
