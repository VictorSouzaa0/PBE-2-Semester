from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "cars"