from django.db import models

# Create your models here.
class Facility(models.Model):
    

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    availability = models.BooleanField(default=True)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name



