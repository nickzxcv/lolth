from django.contrib.gis.db import models

# Create your models here.
class cnty24k09(models.Model):
    name_pcase = models.CharField(max_length=40)
    name_ucase = models.CharField(max_length=30)
    fmname_pc = models.CharField(max_length=40)
    fmname_uc = models.CharField(max_length=26)
    abbrev = models.CharField(max_length=4)
    num = models.IntegerField()
    abcode = models.CharField(max_length=6)
    ansi = models.CharField(max_length=3)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.name_pcase

class plsa_1997(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    plsa_field = models.FloatField()
    plsa_id = models.FloatField()
    section = models.IntegerField()
    meridian = models.CharField(max_length=10)
    township = models.CharField(max_length=5)
    range = models.CharField(max_length=5)
    source = models.CharField(max_length=15)
    comment = models.CharField(max_length=25)
    landgrant = models.CharField(max_length=60)
    town_range = models.CharField(max_length=10)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

class quad24(models.Model):
    quad24_id = models.IntegerField()
    q24code = models.CharField(max_length=9)
    q100cod = models.CharField(max_length=7)
    q250cod = models.CharField(max_length=5)
    quad24name = models.CharField(max_length=50)
    quad24nam2 = models.CharField(max_length=45)
    quad100nam = models.CharField(max_length=50)
    quad250nam = models.CharField(max_length=50)
    state1 = models.CharField(max_length=2)
    state2 = models.CharField(max_length=2)
    state3 = models.CharField(max_length=2)
    state4 = models.CharField(max_length=2)
    x = models.FloatField()
    y = models.FloatField()
    area = models.FloatField()
    corner = models.CharField(max_length=2)
    cell = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    # Returns the string representation of the model.
    def __str__(self):              # __unicode__ on Python 2
        return self.quad24name

class cave(models.Model):
	name = models.CharField(max_length=80)
	aka = models.ForeignKey('self')
	def __str__(self):              # __unicode__ on Python 2
		return self.name

class entrance(models.Model):
	name = models.CharField(max_length=80)
	cave_id = models.ForeignKey('caves')
	location = models.PointField(srid=4326)
	def __str__(self):              # __unicode__ on Python 2
		return self.name

