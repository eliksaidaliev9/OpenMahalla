from django.db import models


class Category(models.Model):
    # Category name, unique=True → must be unique
    title = models.CharField(max_length=155, unique=True)
    # Whether the category is active or not
    is_active = models.BooleanField(default=True)

    # Displaying a model object as a string (e.g. in the admin panel)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories" # Category title in the admin panel