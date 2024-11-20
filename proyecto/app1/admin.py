from django.contrib import admin

# Register your models here.
from .models import Modalidad, Carrera

admin.site.register(Modalidad)
admin.site.register(Carrera)
