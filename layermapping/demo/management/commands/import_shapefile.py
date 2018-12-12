from django.core.management.base import BaseCommand

import logging

from django.contrib.gis.utils import LayerMapping

from demo.models import DemoGeoModel

logger = logging.getLogger(__name__)


DEMO_GEO_MODEL_LAYER_MAPPING = {
    'geom': 'POLYGON',
    'uuid': 'UUID',
    'fill_color': 'FILL_COLOR',
    'name': 'NAME',
    'fill_opacity': 'FILL_OPACI',
    'some_number': 'SOME_NUMBE',
}


def import_shapefile(shapefile_name, layer_mapping):
    DemoGeoModel.objects.all().delete()
    import_layer_map = LayerMapping(DemoGeoModel,
                                    shapefile_name,
                                    layer_mapping)
    import_layer_map.save()


class Command(BaseCommand):
    help = """Import DemoGeoModel objects from the given shapefile.
    """

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('shapefile')

    def handle(self, *args, **options):
        shapefile_name = options['shapefile']
        if not shapefile_name.endswith('.shp'):
            logger.error('Provided file should be a Shapefile with the extension .shp')
            return

        import_shapefile(shapefile_name, DEMO_GEO_MODEL_LAYER_MAPPING)
