from django.db import models

class UrineStripImage(models.Model):
    image = models.ImageField(upload_to='images/')
