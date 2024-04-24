from django.db import models

# Create your models here.

class blogcontentlist (models.Model):
    content = models.CharField (max_length=100)
    desc = models.CharField (max_length= 100)