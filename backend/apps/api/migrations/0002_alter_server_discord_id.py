# Generated by Django 3.2 on 2021-04-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='discord_id',
            field=models.BigIntegerField(),
        ),
    ]
