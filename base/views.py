from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

rooms=[
    {'id':1,'name':'Lets learn Technical Analysis'},
    {'id':2,'name':'lets learn baics of Options'},
    {'id':3,'name':'Basics of Swing Trading'},
]

def home(request):
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room=i
        context={'room':room}
    return render(request,'base/room.html',context)
