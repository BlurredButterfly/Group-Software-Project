# Generated by Django 4.0.2 on 2022-03-23 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_player_lobby_gamestate_task_player_lobby_player_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='playerName',
        ),
    ]