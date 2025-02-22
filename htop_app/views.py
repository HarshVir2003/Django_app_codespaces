from django.shortcuts import render, HttpResponse

# Create your views here.
def index(reqesut):
    return HttpResponse('hi there')