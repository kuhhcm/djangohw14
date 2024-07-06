from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.urls import reverse_lazy


class TodoListView(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'todos'
    
    
class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'create.html'
    success_url = reverse_lazy('list')

    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('list')
    pk_url_kwarg = 'id'

    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('list')
    context_object_name = 'todo'
    pk_url_kwarg = 'id'