# Generated by Django 4.1.1 on 2022-11-29 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_game_details_game_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload/game/file')),
            ],
        ),
    ]
