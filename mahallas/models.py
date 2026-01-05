from django.db import models

class Mahalla(models.Model):
    name = models.CharField(max_length=150)
    district = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name} ({self.district})"