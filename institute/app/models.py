from django.db import models

# Create your models here.
class Institute(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='image')
