# Generated by Django 2.2.5 on 2022-06-01 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_auto_20220601_1453"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.Amenity"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="facilities",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.Facility"
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="room_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rooms",
                to="rooms.RoomType",
            ),
        ),
        migrations.AlterField(
            model_name="room",
            name="rules",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="rooms.HouseRule"
            ),
        ),
    ]
