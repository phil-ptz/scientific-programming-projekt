from django.db import models

# Create your models here.

class Bild(models.Model):
    bild = models.ImageField(upload_to='bilder/')
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.label} - {self.bild.name}"