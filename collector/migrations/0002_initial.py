# Generated by Django 5.2.3 on 2025-06-13 06:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collector', '0001_initial'),
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectorprofile',
            name='district',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core_app.district', verbose_name='Administered District'),
        ),
    ]
