from django.shortcuts import render
# Create your views here.
from rest_framework import generics

from .models import Todo

from .serializers import TodoSerializer


class CreateTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()
