from django.contrib.gis import admin
from models import cnty24k09, plsa_1997, quad24

admin.site.register(cnty24k09, admin.GeoModelAdmin)
admin.site.register(plsa_1997, admin.GeoModelAdmin)
admin.site.register(quad24, admin.GeoModelAdmin)
