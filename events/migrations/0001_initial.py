# Generated by Django 3.2.23 on 2024-01-01 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('private_group', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='group_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joinable', models.BooleanField(default=True)),
                ('status', models.IntegerField(choices=[(1, 'open'), (2, 'in progress'), (3, 'completed')], default=1)),
                ('game_type', models.IntegerField(choices=[(1, 'Singles'), (2, 'Doubles')], default=1)),
                ('team_selection', models.IntegerField(choices=[(1, 'Random'), (2, 'User Defined')], default=1)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='session_admin', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='events.group')),
                ('players', models.ManyToManyField(related_name='session', through='events.PlayerSession', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='playersession',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.session'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inc', models.IntegerField(default=0)),
                ('team_1_score', models.IntegerField(default=0)),
                ('team_1_player1', models.IntegerField()),
                ('team_1_player2', models.IntegerField(blank=True, null=True)),
                ('team_2_score', models.IntegerField(default=0)),
                ('team_2_player1', models.IntegerField()),
                ('team_2_player2', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='game_admin', to=settings.AUTH_USER_MODEL)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_games', to='events.session')),
            ],
        ),
    ]
