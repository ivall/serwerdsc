from rest_framework import serializers
from django.db.utils import IntegrityError
from rest_framework import status

from .validators import CustomSerializerValidator
from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    name = serializers.SlugField(max_length=64, required=False)

    class Meta(object):
        model = Server
        fields = '__all__'

    def create(self, validated_data):
        try:
            server, created = Server.objects.update_or_create(
                discord_id=validated_data.get('discord_id'),
                defaults=validated_data)
        except IntegrityError:
            raise CustomSerializerValidator(
                'Server with this name already exists.',
                field='name',
                status_code=status.HTTP_409_CONFLICT
            )
        return server