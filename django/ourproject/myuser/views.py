from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def Login(request):
#     return HttpResponse('<h1>hello from login</h1>')

# def Logout(request):
#     return HttpResponse('<h1>hello from logout</h1>')

# def Register(request):
#     return HttpResponse('<h1>hello from register</h1>')
from django.shortcuts import render, redirect
from .models import Trainee, Track

def trainees_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainees/list.html', {'trainees': trainees})

def add_trainee(request):
    tracks = Track.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        track_id = request.POST.get("track")
        track = Track.objects.get(id=track_id)

        Trainee.objects.create(name=name, age=age, track=track)
        return redirect('trainees_list')
    return render(request, 'trainees/add.html', {'tracks': tracks})

def tracks_list(request):
    tracks = Track.objects.all()
    return render(request, 'tracks/list.html', {'tracks': tracks})

def add_track(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Track.objects.create(name=name)
        return redirect('tracks_list')
    return render(request, 'tracks/add.html')

