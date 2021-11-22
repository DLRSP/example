from django.db import models
from filer.fields.image import FilerImageField


class MyBackground(models.Model):
    name = models.CharField(verbose_name="Background", max_length=50, null=True)
    image = FilerImageField(null=True, blank=True, on_delete=models.CASCADE)
