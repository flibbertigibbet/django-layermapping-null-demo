import uuid

from django.contrib.gis.db.models import PolygonField
from django.db import models


class DemoGeoModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    geom = PolygonField(srid=4326, blank=True, null=True)
    fill_color = models.CharField(blank=False, null=False, max_length=20)
    name = models.CharField(blank=True, null=True, max_length=20)
    fill_opacity = models.FloatField(blank=False, null=False)
    some_number = models.FloatField(blank=True, null=True)
