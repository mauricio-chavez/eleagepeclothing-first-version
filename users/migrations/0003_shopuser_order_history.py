# Generated by Django 2.1.2 on 2018-11-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_shoppingcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='order_history',
            field=models.ManyToManyField(blank=True, to='users.ShoppingCart'),
        ),
    ]
