import logging
import os

from django.core.management import call_command
from django.test import TestCase

from demo.models import DemoGeoModel

logger = logging.getLogger(__name__)

TESTDATA_PATH = os.path.join(os.path.dirname(__file__), 'data')


class ImportShapefileTestCase(TestCase):

    def setUp(self):
        """Call management command to import the test shapefile."""
        shapefile = os.path.join(TESTDATA_PATH, 'demo_shapefile', 'demo.shp')
        call_command('import_shapefile', shapefile)

    def test_shapefile_command_imported_objects(self):
        self.assertEqual(3, DemoGeoModel.objects.all().count())
        self.assertEqual(1, DemoGeoModel.objects.filter(name='Philadelphia').count())

    def test_shapefile_command_recognized_nulls(self):
        # Should have three objects: one has 0, another a truthy value, and the third is null
        self.assertEqual(1, DemoGeoModel.objects.filter(some_number__isnull=True).count(),
                         'Should have one DemoGeoModel with a null some_number')
        self.assertEqual(1, DemoGeoModel.objects.filter(some_number__gt=0).count(),
                         'Should have one DemoGeoModel with a some_number value > 0')
        self.assertEqual(1, DemoGeoModel.objects.filter(some_number=0).count(),
                         'Should have one DemoGeoModel with a zero some_number')
