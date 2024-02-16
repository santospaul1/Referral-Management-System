# Generated by Django 4.2.9 on 2024-02-15 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("referral", "0005_remove_patient_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="id_number",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="patient",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]