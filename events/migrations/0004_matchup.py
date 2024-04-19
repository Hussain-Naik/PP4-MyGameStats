# Generated by Django 4.2.11 on 2024-04-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_private_group_group_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_count', models.IntegerField()),
                ('game_index', models.IntegerField()),
                ('team1_player1_index', models.IntegerField()),
                ('team1_player2_index', models.IntegerField()),
                ('team2_player1_index', models.IntegerField()),
                ('team2_player2_index', models.IntegerField()),
            ],
        ),
    ]