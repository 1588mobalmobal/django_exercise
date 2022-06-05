from django.core.management.base import BaseCommand, CommandError
from rooms import models as room_models


class Command(BaseCommand):

    AMENITIES = [
        "Kitchen",
        "Heating",
        "Washer",
        "Wifi",
        "Indoor fireplace",
        "Iron",
        "Laptop friendly workspace",
        "Crib",
        "Self check-in",
        "Carbon monoxide detector",
        "Shampoo",
        "Air conditioning",
        "Dryer",
        "Breakfast",
        "Hangers",
        "Hair dryer",
        "TV",
        "High chair",
        "Smoke detector",
        "Private bathroom",
    ]

    help = "Create Amenities, If you want to change the Amenities List, Check the seed_amenities.py"

    def handle(self, *args, **options):
        amenities = self.AMENITIES
        for amenity in amenities:
            room_models.Amenity.objects.create(name=amenity)
        self.stdout.write(self.style.SUCCESS("Amenities was created successfully"))
