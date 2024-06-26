# Generated by Django 4.2.5 on 2023-10-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fistName', models.TextField(max_length=20)),
                ('lastName', models.TextField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('postalcode', models.IntegerField(max_length=10)),
                ('city', models.TextField(max_length=20)),
                ('phoneNumber', models.IntegerField(max_length=15)),
            ],
        ),
    ]
