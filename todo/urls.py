from django.urls import path

from .views import TaskList, TaskCreate, TaskDelete

urlpatterns = [
    path("", TaskList.as_view(), name="todo_list"),
    path("new_task/", TaskCreate.as_view(), name="todo_create"),
    path("confirm_delete/<int:pk>", TaskDelete.as_view(), name="todo_delete"),
]
