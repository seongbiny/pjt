# Generated by Django 3.2.7 on 2021-10-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actormovies'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='actors',
            field=models.ManyToManyField(related_name='reviews', to='movies.Actor'),
        ),
    ]
