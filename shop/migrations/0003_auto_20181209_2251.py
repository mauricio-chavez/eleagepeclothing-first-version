# Generated by Django 2.1.4 on 2018-12-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181111_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='item',
            name='available_sizes',
            field=models.ManyToManyField(to='shop.Size'),
        ),
    ]