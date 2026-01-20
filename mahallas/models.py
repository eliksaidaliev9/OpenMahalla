from django.db import models

class Mahalla(models.Model):
    title = models.CharField(max_length=150)
    district = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.title} ({self.district})"