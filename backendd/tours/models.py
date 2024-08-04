from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tour(models.Model):
    image = models.URLField(max_length=200)
    header = models.CharField(max_length=200)
    content = models.TextField()
    hashtags = models.ManyToManyField(Hashtag, related_name='tours')

    def __str__(self):
        return self.header