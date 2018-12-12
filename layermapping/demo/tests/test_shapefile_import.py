import logging
import os

from django.core.management import call_command
from django.test import TestCase

from demo.models import DemoGeoModel

logger = logging.getLogger(__name__)

TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'data')


class ImportShapefileTestCase(TestCase):

    def test_import_shapefile_command(self):
        shapefile = os.path.join(TESTDATA_PATH, 'demo_shapefile', 'demo.shp')
        call_command('import_shapefile', shapefile)
        self.assertEqual(3, DemoGeoModel.objects.all().count())
        self.assertEqual(1, DemoGeoModel.objects.filter(name='Philadelphia').count())
        self.assertEqual(1, DemoGeoModel.objects.filter(some_number__gt=0).count())
