# Generated by Django 4.2.2 on 2024-01-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo_profile',
            field=models.ImageField(blank=True, default='photo_profile/default_profile.png', null=True, upload_to='photo_profile/', verbose_name='Фото профиля пользователя'),
        ),
    ]