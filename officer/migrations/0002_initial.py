# Generated by Django 5.2.3 on 2025-06-13 06:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('officer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='officerprofile',
            name='user',
            field=models.OneToOneField(limit_choices_to={'user_type': 'OFFICER'}, on_delete=django.db.models.deletion.CASCADE, related_name='officer_profile', to=settings.AUTH_USER_MODEL, verbose_name='User Account'),
        ),
        migrations.AddConstraint(
            model_name='officerprofile',
            constraint=models.UniqueConstraint(condition=models.Q(('is_hod', True)), fields=('department',), name='unique_hod_per_department'),
        ),
    ]
