# Generated by Django 4.2.11 on 2024-04-18 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='author',
            new_name='host',
        ),
    ]
