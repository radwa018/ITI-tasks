from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def all_tracks(request):
    tracks = [[1,'django'],[2,'flask'],[3,'devops'],[4,'python']]
    return render(request,'track/list.html',context={'tracks':tracks})

def get_track_by_id(request):
    return HttpResponse('<h1>hello from track id</h1>')

def update_track(request,id):
    return HttpResponse(f'<h1>hello from updated track{id}</h1>')

def insert_track(request):
    return render(request,'track/insert.html')

def delete_track(request,id):
    return HttpResponse(f'<h1>deleted{id} track</h1>')