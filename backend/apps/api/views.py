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
    lookup_field = 'discord_id'