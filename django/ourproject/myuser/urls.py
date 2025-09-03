from django.urls import path
from . import views

urlpatterns = [
    # path('login/', Login),
    # path('logout/', Logout),
    # path('Register/', Register),
    path('trainees/', views.trainees_list, name='trainees_list'),
    path('trainees/add/', views.add_trainee, name='add_trainee'),
    path('tracks/', views.tracks_list, name='tracks_list'),
    path('tracks/add/', views.add_track, name='add_track'),

]