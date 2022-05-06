from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms=[
#     {'id':1,'name':'Lets learn Technical Analysis'},
#     {'id':2,'name':'lets learn baics of Options'},
#     {'id':3,'name':'Basics of Swing Trading'},
# ]

def home(request):
    rooms =Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    rooms = Room.objects.get(id=pk)
    context={'rooms':rooms}
    return render(request,'base/room.html',context)

