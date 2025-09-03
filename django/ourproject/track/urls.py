from django.urls import path
from  .views import *
urlpatterns = [
    path('',all_tracks),
    path('Track/',get_track_by_id),
    path('insert/',insert_track,name='inserttrack'),
    path('update/<id>',update_track),
    path('delete/<id>',delete_track),


]