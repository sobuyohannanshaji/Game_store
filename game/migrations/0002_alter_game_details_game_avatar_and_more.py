# Generated by Django 4.1.1 on 2022-11-23 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_details',
            name='game_avatar',
            field=models.ImageField(default=True, upload_to='upload/game/images'),
        ),
        migrations.AlterField(
            model_name='game_details',
            name='game_images',
            field=models.ImageField(default=True, upload_to='upload/game/images'),
        ),
        migrations.AlterField(
            model_name='game_details',
            name='game_video1',
            field=models.FileField(default=True, upload_to='upload/game/videos'),
        ),
        migrations.AlterField(
            model_name='game_details',
            name='game_video2',
            field=models.FileField(default=True, upload_to='upload/game/videos'),
        ),
    ]