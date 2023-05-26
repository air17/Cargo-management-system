# Generated by Django 4.2.1 on 2023-05-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location",
            name="id",
        ),
        migrations.AlterField(
            model_name="location",
            name="zip_code",
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
