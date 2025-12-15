from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    """
    Lista zadań + tworzenie nowego zadania.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer