from django.contrib.gis.db import models

# Create your models here.


class cave(models.Model):
        name = models.CharField(max_length=80)
        aka = models.ForeignKey('self', null=True, blank=True)
        def __str__(self):              # __unicode__ on Python 2
                return self.name

class entrance(models.Model):
        name = models.CharField(max_length=80, null=True, blank=True)
        cave = models.ForeignKey('cave')
        location = models.PointField(srid=4326)
        def __str__(self):              # __unicode__ on Python 2
                return self.cave

