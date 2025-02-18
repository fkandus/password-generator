from django.db import models


# Create your models here.
class Password(models.Model):
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField()
