from django.urls import path

from notes.views import NoteCreate, NotesList, NotePage, NoteEdit, NoteDelete

urlpatterns = [
    path('create/', NoteCreate.as_view(), name='create note'),
    path('create/<int:pk>/', NoteCreate.as_view(), name='create note for tutorial'),
    path('all/', NotesList.as_view(), name='my notes'),
    path('<int:pk>/', NotePage.as_view(), name='current note'),
    path('edit/<int:pk>/', NoteEdit.as_view(), name='edit note'),
    path('delete/<int:pk>/', NoteDelete.as_view(), name='delete note'),
]
