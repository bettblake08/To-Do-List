""" This module hosts the url mappings of the todo api """
from django.urls import path

from .views import CreateTodo, SpecificTodo

urlpatterns = [
    path("todo", CreateTodo.as_view(), name="todo"),
    path("todo/<int:pk>", SpecificTodo.as_view(), name="todo_detail")
]
