# todo/views
from rest_framework import generics
# local imports
from .models import Todo
from .serializers import TodoSerializer


class CreateTodo(generics.ListCreateAPIView):
    """
    View to create a todo and get all Todo items
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        serializer.save()


class SpecificTodo(generics.RetrieveUpdateDestroyAPIView):
    """
    View class for getting, updating or deleting a specific todo
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
