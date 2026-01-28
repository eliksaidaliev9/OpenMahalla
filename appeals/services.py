from django.utils import timezone
from .models import Appeal

# Transfer the application to "Under Review" status
def mark_under_review(appeal):
    # Transfer only applications with status NEW to review status
    if appeal.status == Appeal.Status.NEW:
        appeal.status = Appeal.Status.UNDER_REVIEW # Update status
        # Only store the 'status' field, this is an optimization
        appeal.save(update_fields=['status'])
        return appeal # Returns the updated appeal object

# Reply to the request and change the status to "Answered"
def mark_answered(appeal, answer):
    appeal.status = Appeal.Status.ANSWERED # Change status to answered
    appeal.answer = answer # Save reply text
    appeal.answered_at = timezone.now() # Save response time
    appeal.save(update_fields=['status', 'answer', 'answered_at'])
    return appeal # Returns the updated appeal object