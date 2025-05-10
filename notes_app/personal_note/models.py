from django.db import models
from django.urls import reverse

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])