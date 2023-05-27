# Generated by Django 4.2.1 on 2023-05-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_deal_alter_homeslider_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='btn_name',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='title',
        ),
        migrations.AddField(
            model_name='deal',
            name='btn_name1',
            field=models.CharField(default=1, max_length=40, verbose_name='Button Name 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='btn_name2',
            field=models.CharField(default=1, max_length=40, verbose_name='Button Name 2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='text',
            field=models.TextField(default=1, verbose_name='Text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='title1',
            field=models.CharField(default=1, max_length=60, verbose_name='Title 1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='title2',
            field=models.CharField(default=1, max_length=60, verbose_name='Title 2'),
            preserve_default=False,
        ),
    ]
