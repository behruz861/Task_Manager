from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = {
        ('low', "Малый"),
        ('medium', 'Средний'),
        ('high', 'Высокий')
    }
    STATUS_CHOICES = {
        ('Not completed', 'Не выполнено'),
        ('Completed', 'Выполнено'),
    }
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Not completed')

    def __str__(self):
        return self.title