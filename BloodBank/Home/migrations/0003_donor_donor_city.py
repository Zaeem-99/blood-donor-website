# Generated by Django 5.1.6 on 2025-02-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_donor_user_alter_donor_donor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='donor_city',
            field=models.CharField(default='Thane', max_length=15),
        ),
    ]
