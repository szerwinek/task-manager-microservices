from django.urls import path
from .views import TaskListCreateView, AuthPingView

urlpatterns = [
    path("tasks/", TaskListCreateView.as_view(), name="task-list"),
    path("auth-test/", AuthPingView.as_view(), name="auth-test"),
]
