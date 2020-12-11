from django.urls import path

from notes.views import note_create, all_user_notes, note_page, note_edit, note_delete

urlpatterns = [
    path('create/', note_create, name='create note'),
    path('all/', all_user_notes, name='my notes'),
    path('<int:pk>/', note_page, name='current note'),
    path('edit/<int:pk>/', note_edit, name='edit note'),
    path('delete/<int:pk>/', note_delete, name='delete note'),
]
