# Generated by Django 5.1.3 on 2024-11-24 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('reservation', '0003_alter_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='reservation_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reservation_id', to='reservation.reservation'),
            preserve_default=False,
        ),
    ]