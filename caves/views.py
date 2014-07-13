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
