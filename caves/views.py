from django.http import HttpResponse
from caves.models import cave, entrance
from world.models import cnty24k09, plsa_1997, quad24

def index(request):
	return HttpResponse("Hello, world. You're at the cave index.")

def name(request, cave_id):
	mycave=cave.objects.get(pk=cave_id)
	response="{} ".format(mycave)

	if mycave.aka:
		akalist=[mycave.aka]
	else:
		akalist=cave.objects.filter(aka=mycave.id)
	if len(akalist)>0:
		response+="also known as"
		for akacave in akalist:
			response+=" {}".format(akacave.name)

	return HttpResponse(response)

def entrances(request, cave_id):
	mycave=cave.objects.get(pk=cave_id)
	response="{}: ".format(mycave)
	entrancelist=entrance.objects.filter(cave=mycave.id)

	for caveentrance in entrancelist:
		county=cnty24k09.objects.get(geom__contains=caveentrance.location)
		section=plsa_1997.objects.get(geom__contains=caveentrance.location)
		quad=quad24.objects.get(geom__contains=caveentrance.location)
		response+=" {} entrance is in {} County, {} quad, township {} range {} section {}".format(caveentrance, county, quad, section.township, section.range, section.section )

	return HttpResponse(response)
