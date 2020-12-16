from django.urls import path

from tutorials.views import TutorialCreate, TutorialsList, TutorialPage, TutorialEdit, TutorialDelete, \
    TutorialsUser

urlpatterns = [
    path('create/', TutorialCreate.as_view(), name='create tutorial'),
    path('all/', TutorialsList.as_view(), name='all tutorials'),
    path('all/user/', TutorialsUser.as_view(), name='current user tutorials'),
    path('all/user/<int:pk>/', TutorialsUser.as_view(), name='user tutorials'),
    path('edit/<int:pk>/', TutorialEdit.as_view(), name='edit tutorial'),
    path('<int:pk>/', TutorialPage.as_view(), name='view tutorial page'),
    path('delete/<int:pk>/', TutorialDelete.as_view(), name='delete tutorial')
]
