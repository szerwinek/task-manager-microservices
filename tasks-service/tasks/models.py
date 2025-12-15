from django.db import models


class Task(models.Model):
    """
    Model zadania w tasks-service.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    user_id = models.IntegerField(
        help_text="ID użytkownika z auth-service"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title