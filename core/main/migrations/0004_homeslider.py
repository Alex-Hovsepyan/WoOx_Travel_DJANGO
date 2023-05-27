# Generated by Django 4.2.1 on 2023-05-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_home_options_alter_home_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Immage')),
                ('name', models.CharField(max_length=50, verbose_name='Country Name')),
                ('info1', models.CharField(max_length=50, verbose_name='Info 1')),
                ('info2', models.CharField(max_length=50, verbose_name='Info 2')),
                ('info3', models.CharField(max_length=50, verbose_name='Info 3')),
            ],
            options={
                'verbose_name': 'HomeSlider',
                'verbose_name_plural': 'HomeSlider',
            },
        ),
    ]