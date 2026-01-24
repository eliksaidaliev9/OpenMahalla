from django.db import models
from django.contrib.auth import get_user_model
from mahallas.models import Mahalla
from categories.models import Category

User = get_user_model()

class Appeal(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        UNDER_REVIEW = 'under_review', 'Under review'
        ANSWERED = 'answered', 'Answered'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=155)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='appeals')
    description = models.TextField()
    answer = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_status_display()})"

    @classmethod
    def new(cls):
        return cls.objects.filter(status=cls.Status.NEW)

    @classmethod
    def under_review(cls):
        return cls.objects.filter(status=cls.Status.UNDER_REVIEW)

    @classmethod
    def answered(cls):
        return cls.objects.filter(status=cls.Status.ANSWERED)
