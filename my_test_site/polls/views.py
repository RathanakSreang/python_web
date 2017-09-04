# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello world, you are at Poll app index")

def rathanak(request):
  return HttpResponse("Rathanak Jame 007")
