from django.shortcuts import render

from .models import SpotifyPlaylist

def index(request):
    spotify = SpotifyPlaylist.objects.get(pk=1)
    return render(request,'home/index.html',{'spotify': spotify})

def about(request):
    return render(request,'base.html')
