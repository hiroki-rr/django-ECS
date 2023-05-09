from django.db import models
from django.conf import settings
from activity.models import ActivityRecord

class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    name = models.CharField(max_length=30)
    goal = models.CharField(max_length=255)
    color_code = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}-{self.name},{self.goal}"

class ActivityCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    activity_record = models.ForeignKey(ActivityRecord, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user}-{self.category}{self.activity_record}"
