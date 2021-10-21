from django.db import models


class SiteDetail(models.Model):
    logo = models.ImageField(upload_to='images/')

