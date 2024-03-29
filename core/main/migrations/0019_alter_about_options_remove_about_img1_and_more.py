# Generated by Django 4.2.1 on 2023-05-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_about_title2_colored'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.RemoveField(
            model_name='about',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='about',
            name='img2',
        ),
        migrations.AddField(
            model_name='about',
            name='img',
            field=models.ImageField(default=1, upload_to='images', verbose_name='Background Image'),
            preserve_default=False,
        ),
    ]
