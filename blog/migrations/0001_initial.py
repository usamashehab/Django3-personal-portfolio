# Generated by Django 3.1.5 on 2021-02-02 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=400)),
                ('article', models.TextField()),
                ('url', models.URLField()),
                ('date', models.DateField()),
            ],
        ),
    ]
