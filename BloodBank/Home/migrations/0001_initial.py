# Generated by Django 5.1.6 on 2025-02-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=100)),
                ('donor_email', models.EmailField(max_length=254)),
                ('donor_bloodtype', models.CharField(max_length=3)),
                ('donor_phone', models.CharField(max_length=15)),
            ],
        ),
    ]
