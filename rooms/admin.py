from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin Definition"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "Space",
            {"fields": ("guest", "beds", "bedrooms", "baths")},
        ),
        (
            "More About Space",
            {"classes": ("collapse",), "fields": ("amenities", "facilities", "rules")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    # add list ordering
    # ordering = ("name", "price")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guest",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "rules",
        "city",
        "country",
    )

    search_fields = ("name", "city", "country", "host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Amenities"

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_descriptions = "Photos"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """Photo Admin Definition"""

    pass
