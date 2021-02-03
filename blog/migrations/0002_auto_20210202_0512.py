# Generated by Django 3.1.5 on 2021-02-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.AlterField(
            model_name='blog',
            name='article',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
