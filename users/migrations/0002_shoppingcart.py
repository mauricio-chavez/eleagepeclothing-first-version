# Generated by Django 2.1.2 on 2018-11-11 23:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20181111_2314'),
        ('users', '0001_initial'),
    ]

    operations = [
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
