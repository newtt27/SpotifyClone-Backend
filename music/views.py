from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_music(request):
    return HttpResponse("This is the music data")
