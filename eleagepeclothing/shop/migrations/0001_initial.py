# Generated by Django 2.1.2 on 2018-11-11 23:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('pub_date', models.DateField(default=django.utils.timezone.now, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('short_description', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(max_length=200, null=True, upload_to=shop.models.get_image_path)),
                ('category', models.ManyToManyField(blank=True, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prices_sum', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10)),
                ('bought', models.BooleanField(blank=True, default=False)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('items', models.ManyToManyField(blank=True, to='shop.Item')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.ShopUser')),
            ],
        ),
    ]
