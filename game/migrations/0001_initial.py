# Generated by Django 4.0.1 on 2022-02-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobby_code', models.CharField(max_length=18, unique=True)),
            ],
        ),
    ]
