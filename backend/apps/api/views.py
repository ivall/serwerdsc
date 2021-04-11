from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .permissions import AccessPermission

from .serializers import ServerSerializer
from .models import Server


class ServerViewSet(ModelViewSet):
    permission_classes = [AccessPermission]
    serializer_class = ServerSerializer
    queryset = Server.objects.all()

    def retrieve(self, request, *args, **kwargs):
        discord_id = kwargs['pk']  # id of discord server
        server = get_object_or_404(Server, discord_id=discord_id)
        serializer = self.serializer_class(server)
        return Response(serializer.data)