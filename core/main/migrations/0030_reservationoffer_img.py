# Generated by Django 4.2.1 on 2023-05-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_reservationoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationoffer',
            name='img',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Background Image'),
            preserve_default=False,
        ),
    ]
