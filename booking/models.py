from django.db import models


class Booking(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.ImageField(upload_to='booking/')


    def __str__(self):
        return self.title
