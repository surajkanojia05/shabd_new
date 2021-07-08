from django.contrib import admin
from .models import ghazal_home
from .models import famous_ghazal
from .models import new_ghazal

# Register your models here.

admin.site.register(ghazal_home)
admin.site.register(famous_ghazal)
admin.site.register(new_ghazal)