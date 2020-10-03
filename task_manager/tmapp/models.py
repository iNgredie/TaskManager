from django.contrib.auth.models import User
from django.db import models
from simple_history.models import HistoricalRecords


class UserTask(models.Model):
    status_choices = [
        ('New', 'New'),
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choices, max_length=255)
    deadline = models.DateTimeField(auto_now_add=False, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.owner