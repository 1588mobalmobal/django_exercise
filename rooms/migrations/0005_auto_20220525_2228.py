# Generated by Django 2.2.5 on 2022-05-25 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0004_auto_20220525_2213"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="rooms.Room"
            ),
        ),
    ]
