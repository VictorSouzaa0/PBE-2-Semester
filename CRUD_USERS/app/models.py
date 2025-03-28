from django.db import models
from django.contrib.auth.models import AbstractUser

class userAbs(AbstractUser):
    phone = models.PositiveIntegerField(blank=True,null=True),
    function = models.CharField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.username