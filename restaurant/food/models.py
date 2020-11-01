from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/blog/image')
    price = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
