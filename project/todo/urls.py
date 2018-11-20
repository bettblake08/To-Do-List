""" This module hosts the url mappings of the todo api """
from django.urls import path

from .views import CreateTodo
"""
Example:
urlpatterns = [
    path('/', views.index)
]
"""

urlpatterns = [
    path("todo", CreateTodo.as_view(), name="todo"),
]