# Generated by Django 4.0.2 on 2022-03-23 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_remove_lobby_lobby_code_lobby_lobby_name_lobby_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.CharField(default='Guest', max_length=200)),
                ('isImposter', models.BooleanField(default=False)),
                ('isAlive', models.BooleanField(default=False)),
                ('gpsLongitude', models.FloatField(default=0)),
                ('gpsLatitude', models.FloatField(default=0)),
                ('color', models.CharField(default='#000000', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='lobby',
            name='gameState',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(default='Task', max_length=200)),
                ('gpsLongitude', models.FloatField(default=0)),
                ('gpsLatitude', models.FloatField(default=0)),
                ('taskNumber', models.IntegerField(default=0)),
                ('isDone', models.BooleanField(default=False)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.player')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='lobby',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.lobby'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
