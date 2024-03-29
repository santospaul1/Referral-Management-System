# Generated by Django 4.2.9 on 2024-02-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("referral", "0015_alter_disease_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="referral",
            name="diseases",
            field=models.ManyToManyField(null=True, to="referral.disease"),
        ),
        migrations.AlterField(
            model_name="disease",
            name="name",
            field=models.CharField(default=None, max_length=50),
        ),
    ]
