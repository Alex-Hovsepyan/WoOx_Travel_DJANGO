# Generated by Django 4.2.1 on 2023-05-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_about_options_remove_about_img1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Image')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
    ]
