# Generated by Django 2.1.4 on 2018-12-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181207_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifyplaylist',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
