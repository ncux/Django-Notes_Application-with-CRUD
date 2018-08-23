from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Q


from .models import Note
from .forms import NoteModelForm


@login_required
def create_note_view(request):
    form = NoteModelForm()
    if request.method == 'POST':
        form = NoteModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.info(request, 'Note successfully created!')
            return redirect('notes:all-notes')

    template = 'notes/create_new_note.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def all_notes_view(request):
    all_notes = Note.objects.filter(user=request.user)
    query = request.GET.get('search')
    if query:
        all_notes = all_notes.filter(Q(title__icontains=query))
    context = {'notes': all_notes}
    template = 'notes/all_notes.html'
    return render(request, template, context)


@login_required
def note_detail_view(request, pk):
    note = get_object_or_404(Note, pk=pk)
    context = {'note': note}
    template = 'notes/note_detail.html'
    return render(request, template, context)


class NoteUpdateView(LoginRequiredMixin, UpdateView):      # inherit LoginRequiredMixin first!
    model = Note
    template_name = 'notes/update_note.html'
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('notes:all-notes')


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes/delete_note.html'
    success_url = reverse_lazy('notes:all-notes')
