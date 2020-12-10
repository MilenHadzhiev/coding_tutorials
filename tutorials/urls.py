from django.urls import path

from tutorials.views import tutorial_create, tutorial_edit, tutorial_page, tutorials_all, tutorials_user, \
    tutorial_delete

urlpatterns = [
    path('create/', tutorial_create, name='create tutorial'),
    path('all/', tutorials_all, name='all tutorials'),
    path('all/user/', tutorials_user, name='current user tutorials'),
    path('all/user/<int:pk>/', tutorials_user, name='user tutorials'),
    path('edit/<int:pk>/', tutorial_edit, name='edit tutorial'),
    path('<int:pk>/', tutorial_page, name='view tutorial page'),
    path('delete/<int:pk>/', tutorial_delete, name='delete tutorial')
]
