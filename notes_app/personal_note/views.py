from django.shortcuts import render
from .models import Note
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.

class Note_List_view(ListView):
    model = Note
    template_name = 'list.html'
    context_object_name='notes'    #it is important to use this name notes here if not its default set to objects

    def get_queryset(self):
        # Get the search query from the GET request
        query = self.request.GET.get('q')
        if query:
            # Filter notes by title if there's a query
            return Note.objects.filter(title__icontains=query)
        else:
            # Return all notes if no query is present
            return Note.objects.all()
        
        
class Note_detail_view(DetailView):
    model = Note
    template_name = 'detail.html'
    context_object_name = 'note'  #important to use note here check once 

class Note_create_view(CreateView):
    model = Note
    template_name = 'create.html'
    fields = ['title','content']

class Note_edit_view(UpdateView):
    model = Note
    template_name = 'edit.html'
    fields = ['title','content']

class Note_delete_view(DeleteView):
    model = Note
    template_name = 'delete.html'
    context_object_name = 'note'
    success_url=reverse_lazy('list_view')