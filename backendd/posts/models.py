from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.email})'
    
    