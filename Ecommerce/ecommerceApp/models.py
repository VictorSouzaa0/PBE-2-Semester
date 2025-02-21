from django.db import models


class Ecommerce(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name