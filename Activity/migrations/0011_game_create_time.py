# Generated by Django 2.1.2 on 2018-10-18 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0010_remove_game_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
