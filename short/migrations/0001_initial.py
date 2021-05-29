# Generated by Django 3.2.3 on 2021-05-29 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myurl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.URLField(max_length=2048, unique=True, verbose_name='Long URL')),
                ('shorturl', models.URLField(max_length=2048, unique=True, verbose_name='Short URL')),
                ('desc', models.CharField(max_length=400, verbose_name='Description')),
            ],
        ),
    ]