from django.contrib import admin
from .models import Room

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display=('room_no',"price","capacity","type")

admin.site.register(Room,RoomAdmin)