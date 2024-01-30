from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Note


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notes/note_list.html'

class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'content', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = ['title', 'content', 'tags']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')


