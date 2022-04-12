from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    owner = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, help_text='Enter the title of your task')
    content = models.TextField(max_length=1000, blank=True, null=True, help_text='Enter your task')
    complete = models.BooleanField(default=False)
    date_create = models.DateField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
