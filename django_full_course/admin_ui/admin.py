from django.contrib import admin
from .models import Laptop


# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ("brand", "os_type", "color", "price")
    list_filter = ("os_type", "color")
    search_fields = ("brand", "os_type")
    ordering = ("os_type",)


admin.site.register(Laptop, LaptopAdmin)
