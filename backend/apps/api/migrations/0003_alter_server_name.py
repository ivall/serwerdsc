# Generated by Django 3.2 on 2021-04-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_server_discord_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]