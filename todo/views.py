from typing import Optional
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from .models import Todo


class TaskList(LoginRequiredMixin, ListView):
    model = Todo
    template_name = "todo/todo_list.html"
    context_object_name = "tasks"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Todo
    template_name = "todo/todo_create.html"
    success_url = reverse_lazy("todo_list")
    fields = ["text"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class TaskDelete(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Todo
    template_name = "todo/todo_delete.html"
    success_url = reverse_lazy("todo_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")