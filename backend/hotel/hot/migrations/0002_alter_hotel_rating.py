# Generated by Django 5.1.3 on 2024-11-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=None),
        ),
    ]
