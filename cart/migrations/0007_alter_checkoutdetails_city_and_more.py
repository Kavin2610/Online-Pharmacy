# Generated by Django 4.2.5 on 2023-10-05 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_checkoutdetails_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutdetails',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='fistName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='lastName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='checkoutdetails',
            name='postalcode',
            field=models.IntegerField(),
        ),
    ]
