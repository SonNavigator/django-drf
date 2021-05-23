from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)  # Auto timestamp
    complete = models.BooleanField(default=False)

    # Convert an object to readable string
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_on']


