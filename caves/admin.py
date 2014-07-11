from django.contrib.gis import admin
from models import cave, entrance

# Register your models here.
admin.site.register(cave, admin.GeoModelAdmin)
admin.site.register(entrance, admin.GeoModelAdmin)

