from django.contrib.gis.db import models

class cave(models.Model):
	# every cave needs a name
	# alternate names must refer to some other cave
	# but not every cave is itself an alternate name
        name = models.CharField(max_length=80)
        aka = models.ForeignKey('self', null=True, blank=True)
        def __str__(self):              # __unicode__ on Python 2
                return self.name

class entrance(models.Model):
	# not every entrance has a name
	# but every entrance must have a cave that has a name
        name = models.CharField(max_length=80, null=True, blank=True)
        cave = models.ForeignKey('cave')
        location = models.PointField(srid=4326)
        def __str__(self):              # __unicode__ on Python 2
		if not self.name:
	                return self.cave.name
		else:
			return self.name

