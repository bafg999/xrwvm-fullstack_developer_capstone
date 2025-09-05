from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.
admin.site.register(CarMake)
admin.site.register(CarModel)

# CarModelInline class
class CarModelInline(admin.TabularInline):  # Puede ser también StackedInline
    model = CarModel
    extra = 1

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ("name", "car_make", "dealer_id")  # columnas en la tabla
    search_fields = ("name",)  # permite buscar por nombre
    list_filter = ("car_make",)  # permite filtrar por fabricante

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")  # columnas en la tabla
    search_fields = ("name",)  # búsqueda por nombre
    inlines = [CarModelInline]  # agrega CarModel dentro de CarMake

# Register models here
