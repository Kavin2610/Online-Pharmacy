# Generated by Django 4.2.5 on 2024-01-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_cartitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
