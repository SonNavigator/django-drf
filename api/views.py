from .serializers import TaskSerializer
from .models import Task
from rest_framework import generics, permissions


# Function Based Views (We no longer use)
"""
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
"""


# Instead we use Class Based Views (CBV) to
# utilize more features
# class TaskList(generics.ListAPIView):
    # queryset = Task.objects.all()
    # serializer_class = TaskSerializer
    # permission_classes = (AllowAny,)

# /api/tasks/ --> Not require id
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()  # required
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# /api/tasks/ --> Required id
class TaskDetail(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

