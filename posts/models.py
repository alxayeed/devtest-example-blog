from django.db import models

# Create your models here.


class Comment(models.Model):
    '''
    Model class for comment by the user
    '''
    post_id = models.CharField(max_length=3)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.body
