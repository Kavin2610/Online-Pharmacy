# Generated by Django 5.0.1 on 2024-03-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_alter_coupon_usage_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient_name',
            field=models.CharField(max_length=25),
        ),
    ]