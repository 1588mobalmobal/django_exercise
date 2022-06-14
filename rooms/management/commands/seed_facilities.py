from django.core.management.base import BaseCommand, CommandError
from rooms import models as room_models


class Command(BaseCommand):

    FACILITIES = [
        "Private entrance",
        "Paid Parking on premises",
        "Paid parking off premises",
        "Elevator",
        "Parking",
        "Gym",
    ]

    help = "Create Amenities, If you want to change the Amenities List, Check the seed_amenities.py"

    def handle(self, *args, **options):
        facilities = self.FACILITIES
        for facility in facilities:
            room_models.Facility.objects.create(name=facility)
        self.stdout.write(
            self.style.SUCCESS(f"{len(facilities)} Facilities was created successfully")
        )
