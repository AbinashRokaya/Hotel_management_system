# Generated by Django 5.1.3 on 2024-11-24 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hot', '0002_alter_hotel_rating'),
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='hotel_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hot_id', to='hot.hotel'),
        ),
    ]
