from django.db import models

class posts(models.Model):
  POST_INCLUDE={
    "TOP":"TOPIC",
    "CONT":"CONTENT",
    "AUTH":"AUTHOR",
    "IMG":"IMAGE" 
  }
  topic = models.CharField(max_length=255)
  content = models.CharField(max_length=255)
  author = models.CharField(max_length=255, default='anonymous')
  image = models.ImageField(upload_to='images/', null=True, blank=True) # Handle the image file

