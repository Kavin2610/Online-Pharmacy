# Generated by Django 5.0.1 on 2024-02-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_phone_number_userprofile_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
