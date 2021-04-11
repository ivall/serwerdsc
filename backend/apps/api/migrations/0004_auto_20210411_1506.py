# Generated by Django 3.2 on 2021-04-11 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_server_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='discord_avatar',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='server',
            name='discord_invite',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='server',
            name='discord_name',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='server',
            name='css_file',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='server',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(blank=True, max_length=64, unique=True),
        ),
    ]
