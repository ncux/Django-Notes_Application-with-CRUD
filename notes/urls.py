
from django.urls import path
from .views import all_notes_view, note_detail_view, create_note_view, NoteUpdateView, NoteDeleteView

app_name = "notes"

urlpatterns = [
    path('create', create_note_view, name='create-note'),
    path('list', all_notes_view, name='all-notes'),
    path('detail/<int:pk>', note_detail_view, name='note-detail'),
    path('update/<int:pk>', NoteUpdateView.as_view(), name='update-note'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='delete-note'),

]


