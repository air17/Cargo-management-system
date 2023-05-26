# Generated by Django 4.2.1 on 2023-05-25 10:22
import csv

from django.db import migrations

from core.settings.components import BASE_DIR

BATCH_SIZE = 1000


def load_locations(apps, schema_editor):
    Location = apps.get_model("location", "Location")
    with open(BASE_DIR.joinpath("apps/location/uszips.csv"), "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        batch = []
        for row in reader:
            batch.append(Location(zip_code=row[0], latitude=row[1], longitude=row[2], city=row[3], state=row[5]))
            if len(batch) >= BATCH_SIZE:
                Location.objects.bulk_create(batch)
                batch = []
        if batch:
            Location.objects.bulk_create(batch)


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0002_remove_location_id_alter_location_zip_code"),
    ]

    operations = [
        migrations.RunPython(load_locations),
    ]
