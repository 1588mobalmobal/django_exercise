import random
from django.contrib.admin.utils import flatten
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(100, 1000),
                "guest": lambda x: random.randint(1, 10),
                "beds": lambda x: random.randint(1, 10),
                "bedrooms": lambda x: random.randint(1, 10),
                "baths": lambda x: random.randint(1, 10),
            },
        )
        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for serial in created_clean:
            room = room_models.Room.objects.get(id=serial)
            for i in range(3, random.randint(6, 9)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                    room=room,
                )
        self.stdout.write(self.style.SUCCESS(f"{number} rooms was created!"))
