from django.db import models

class Mahalla(models.Model):
    title = models.CharField(max_length=150)  # Mahalla title
    district = models.CharField(max_length=150)  # Which district does it belong to

    def __str__(self):
        return f"{self.title} ({self.district})"  # Representing the model as a string