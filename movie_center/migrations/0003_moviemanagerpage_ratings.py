# Generated by Django 3.0.2 on 2020-01-31 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_center', '0002_auto_20200131_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemanagerpage',
            name='ratings',
            field=models.CharField(choices=[('G', 'General Audience'), ('PG', 'PG'), ('PG-13', 'PG-13')], default='G', max_length=32),
        ),
    ]
