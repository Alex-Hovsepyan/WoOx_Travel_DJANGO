# Generated by Django 4.2.1 on 2023-05-27 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_dealcontent_to_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealcontent',
            name='to_check_slider',
            field=models.BooleanField(blank=True, default=1, verbose_name='To Check For Slider'),
            preserve_default=False,
        ),
    ]