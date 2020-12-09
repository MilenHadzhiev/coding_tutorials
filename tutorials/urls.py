from django.urls import path

from tutorials.views import tutorial_create, tutorials

urlpatterns = [
    path('create/', tutorial_create, name='create tutorial'),
    path('tutorials/', tutorials, name='current user tutorials'),
    path('tutorials/<int:pk>', tutorials, name='all tutorials'),
]