# Generated by Django 4.2.5 on 2024-01-12 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0009_alter_rating_score'),
        ('cart', '0011_alter_cartitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='Item',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, to='item.item'),
        ),
    ]
