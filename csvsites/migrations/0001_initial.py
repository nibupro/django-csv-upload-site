# Generated by Django 3.0.4 on 2020-03-10 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_title', models.CharField(max_length=100)),
                ('artist_names', models.CharField(max_length=100)),
                ('album_name', models.CharField(max_length=100)),
                ('release_date', models.DateField(verbose_name='music released')),
            ],
        ),
    ]