from django.utils import timezone
from .models import Appeal


def mark_under_review(appeal):
    if appeal.status == Appeal.Status.NEW:
        appeal.status = Appeal.Status.UNDER_REVIEW
        appeal.save(update_fields=['status'])
        return appeal

def mark_answered(appeal, answer):
    appeal.status = Appeal.Status.ANSWERED
    appeal.answer = answer
    appeal.answered_at = timezone.now()
    appeal.save(update_fields=['status', 'answer', 'answered_at'])
    return appeal