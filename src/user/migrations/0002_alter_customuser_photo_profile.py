# Generated by Django 4.2.2 on 2024-01-28 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo_profile',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='photo_profile/', verbose_name='Фото профиля пользователя'),
        ),
    ]
