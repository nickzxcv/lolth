import os
from django.contrib.gis.utils import LayerMapping
from models import cnty24k09, cnty24k09_mapping, plsa_1997, plsa_1997_mapping, quad24, quad24_mapping

cnty24k09_shp=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/cnty24k09/shapefiles/cnty24k09_1_multipart.shp'))
plsa_1997_shp=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/plsa_1997/plsa/plsa.shp'))
quad24_shp=os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/quad24/quad24.shp'))

def run(verbose=True):
    lm = LayerMapping(cnty24k09, cnty24k09_shp, cnty24k09_mapping,
                      source_srs='+proj=aea +lat_1=34 +lat_2=40.5 +lat_0=0 +lon_0=-120 +x_0=0 +y_0=-4000000 +ellps=GRS80 +datum=NAD83 +units=m +no_defs ', encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(plsa_1997, plsa_1997_shp, plsa_1997_mapping,
                      source_srs='+proj=aea +lat_1=34 +lat_2=40.5 +lat_0=0 +lon_0=-120 +x_0=0 +y_0=-4000000 +ellps=GRS80 +datum=NAD83 +units=m +no_defs ', encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
    lm = LayerMapping(quad24, quad24_shp, quad24_mapping,
                      source_srs=4269, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
