import os
from django.contrib.gis.utils import LayerMapping
from models import cnty24k09, plsa_1997, quad24

# Auto-generated `LayerMapping` dictionary for cnty24k09 model
cnty24k09_mapping = { 
    'name_pcase' : 'NAME_PCASE',
    'name_ucase' : 'NAME_UCASE',
    'fmname_pc' : 'FMNAME_PC',
    'fmname_uc' : 'FMNAME_UC',
    'abbrev' : 'ABBREV',
    'num' : 'NUM',
    'abcode' : 'ABCODE',
    'ansi' : 'ANSI',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}
# Auto-generated `LayerMapping` dictionary for plsa_1997 model
plsa_1997_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'plsa_field' : 'PLSA_',
    'plsa_id' : 'PLSA_ID',
    'section' : 'SECTION',
    'meridian' : 'MERIDIAN',
    'township' : 'TOWNSHIP',
    'range' : 'RANGE',
    'source' : 'SOURCE',
    'comment' : 'COMMENT',
    'landgrant' : 'LANDGRANT',
    'town_range' : 'TOWN_RANGE',
    'geom' : 'MULTIPOLYGON',
}
# Auto-generated `LayerMapping` dictionary for quad24 model
quad24_mapping = {
    'quad24_id' : 'QUAD24_ID',
    'q24code' : 'Q24CODE',
    'q100cod' : 'Q100COD',
    'q250cod' : 'Q250COD',
    'quad24name' : 'QUAD24NAME',
    'quad24nam2' : 'QUAD24NAM2',
    'quad100nam' : 'QUAD100NAM',
    'quad250nam' : 'QUAD250NAM',
    'state1' : 'STATE1',
    'state2' : 'STATE2',
    'state3' : 'STATE3',
    'state4' : 'STATE4',
    'x' : 'X',
    'y' : 'Y',
    'area' : 'AREA',
    'corner' : 'CORNER',
    'cell' : 'CELL',
    'geom' : 'MULTIPOLYGON',
}

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
