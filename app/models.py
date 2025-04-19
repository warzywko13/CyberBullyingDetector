from django.db import models
from django.utils import timezone

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    is_toxic = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    def as_dict(self):
        return {
            "id":         self.id,
            "comment":    self.comment,
            "is_toxic":   self.is_toxic,
        }