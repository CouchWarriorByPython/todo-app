from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import TodoSerializer
from .models import Todo


class TodoListViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        complete = self.request.query_params.get('complete', None)
        if complete is not None:
            queryset = Todo.objects.filter(complete=complete.title(), owner=request.user)
        else:
            queryset = Todo.objects.filter(owner=request.user)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        if self.get_object().owner == request.user:
            return Response(self.get_serializer(self.get_object()).data)
        else:
            return Response({'message': 'not found'}, status=403)
