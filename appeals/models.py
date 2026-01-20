from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from mahallas.models import Mahalla

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title

class Appeal(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'New'
        UNDER_REVIEW = 'under_review', 'Under review'
        ANSWERED = 'answered', 'Answered'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    answer = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"

    @classmethod
    def new(cls):
        return cls.objects.filter(status=cls.Status.NEW)

    @classmethod
    def under_review(cls):
        return cls.objects.filter(status=cls.Status.UNDER_REVIEW)

    @classmethod
    def answered(cls):
        return cls.objects.filter(status=cls.Status.ANSWERED)

    def mark_under_review(self):
        self.status = self.Status.UNDER_REVIEW
        self.save(update_fields=['status'])

    def mark_answered(self, answer_text: str = ''):
        self.status = self.Status.ANSWERED
        if answer_text:
            self.answer = answer_text
        self.answered_at = timezone.now()
        self.save(update_fields=['status', 'answer', 'answered_at'])