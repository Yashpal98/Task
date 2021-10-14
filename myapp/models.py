from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    image =  models.ImageField(upload_to='images')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    unliked = models.ManyToManyField(User, default=None, blank=True, related_name="unliked")

    def __str__(self):
        return self.title
    
    @property
    def num_likes(self):
        return self.liked.all().count()

    @property
    def num_unlikes(self):
        return self.unliked.all().count()

LIKED_CHOICES = (
    ('like','like'),
    ('unlike','unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKED_CHOICES, default='like', max_length=10)
    
    def __str__(self):
        return str(self.feed)

class Unlike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKED_CHOICES, default='unlike', max_length=10)
    
    def __str__(self):
        return str(self.feed)
    