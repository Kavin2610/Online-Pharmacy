# Generated by Django 4.2.5 on 2023-10-05 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_checkoutdetails_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdetails',
            old_name='fistName',
            new_name='firstName',
        ),
    ]
