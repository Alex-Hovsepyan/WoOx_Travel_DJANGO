# Generated by Django 4.2.1 on 2023-05-27 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='img',
        ),
        migrations.AddField(
            model_name='about',
            name='img1',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Background Image 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='img2',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Background Image 2'),
            preserve_default=False,
        ),
    ]
