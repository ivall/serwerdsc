from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=True)
    description = models.CharField(max_length=512, blank=True)
    css_file = models.URLField(blank=True)

    discord_id = models.BigIntegerField()
    discord_invite = models.URLField(blank=True)
    discord_name = models.CharField(max_length=32, blank=True)
    discord_avatar = models.URLField(blank=True)
