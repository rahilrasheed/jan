from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fncod(request):
    return HttpResponse("hello iam rahil")
def fnfile(request):
    return  render(request,'file.html')