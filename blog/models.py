from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.title) + " | " + str(self.author)

    def publish(self):
        self.published_on = timezone.now()
        self.save()


