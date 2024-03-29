# Generated by Django 4.2.9 on 2024-02-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("referral", "0010_hospital_email_alter_hospital_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default=None, max_length=50)),
                ("description", models.TextField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="hospital",
            name="password",
            field=models.CharField(default=None, max_length=30),
        ),
    ]
