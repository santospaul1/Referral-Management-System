# Generated by Django 4.2.9 on 2024-02-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("referral", "0013_hospital_diseases"),
    ]

    operations = [
        migrations.RemoveField(model_name="hospital", name="user",),
        migrations.AddField(
            model_name="hospital",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="hospital",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="hospital",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
        migrations.RemoveField(model_name="hospital", name="diseases",),
        migrations.AlterField(
            model_name="hospital",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="hospital",
            name="location",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="hospital",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AddField(
            model_name="hospital",
            name="diseases",
            field=models.ManyToManyField(null=True, to="referral.disease"),
        ),
    ]
