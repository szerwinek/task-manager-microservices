from rest_framework.views import APIView
from rest_framework.response import Response


class TaskListCreateView(APIView):
    def get(self, request):
        return Response(
            {
                "tasks": [
                    {"id": 1, "title": "First task"},
                    {"id": 2, "title": "Second task"},
                ]
            }
        )


class AuthPingView(APIView):
    def get(self, request):
        return Response(
            {
                "status": "auth service reachable",
            }
        )
