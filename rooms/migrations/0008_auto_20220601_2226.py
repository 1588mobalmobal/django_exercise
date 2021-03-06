# Generated by Django 2.2.5 on 2022-06-01 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0007_auto_20220601_2209"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rooms",
                to="rooms.Room",
            ),
        ),
    ]
