# Generated by Django 4.2.1 on 2023-05-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_deal_btn_name_remove_deal_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Image')),
                ('country', models.CharField(max_length=60, verbose_name='Country')),
                ('place', models.CharField(max_length=60, verbose_name='Place')),
                ('text', models.TextField(verbose_name='Text')),
                ('people', models.CharField(max_length=30, verbose_name='People')),
                ('area', models.CharField(max_length=30, verbose_name='Area')),
                ('money', models.CharField(max_length=25, verbose_name='Money')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('days', models.CharField(max_length=20, verbose_name='Days')),
            ],
        ),
    ]
