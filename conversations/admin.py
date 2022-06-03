from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Configuration"""

    list_display = ("__str__", "count_messages", "count_participants")


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Configuration"""

    list_display = ("__str__", "created")
