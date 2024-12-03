from django.contrib import admin
from .models import Reservation

# Register your models here.
class RevervationAdmin(admin.ModelAdmin):
    list_display=('check_in','check_out','status')

admin.site.register(Reservation,RevervationAdmin)
