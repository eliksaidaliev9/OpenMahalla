from django.db import models
from django.contrib.auth import get_user_model
from mahallas.models import Mahalla
from categories.models import Category

User = get_user_model() # Getting a custom user model in Django

class Appeal(models.Model):
    # STATUS ENUM: To specify the status of the request
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        UNDER_REVIEW = 'under_review', 'Under review'
        ANSWERED = 'answered', 'Answered'
    # User(applicant)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Full name and surname
    full_name = models.CharField(max_length=155)
    # Connecting to the Mahalla model (foreignKey)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    # Connecting to the Category model (foreignKey)
    # If category is deleted, it may be null
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='appeals')
    # Text of the appeal
    description = models.TextField()
    # Response text (can be empty)
    answer = models.TextField(blank=True)
    # Status (field restricted by choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    # The time the request was created
    created_at = models.DateTimeField(auto_now_add=True)
    # The time of response to the request
    answered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        # Show model as string
        return f"{self.full_name} ({self.get_status_display()})"
    # The following classmethods are used to filter requests by status
    @classmethod
    def new(cls):
        return cls.objects.filter(status=cls.Status.NEW)

    @classmethod
    def under_review(cls):
        return cls.objects.filter(status=cls.Status.UNDER_REVIEW)

    @classmethod
    def answered(cls):
        return cls.objects.filter(status=cls.Status.ANSWERED)
