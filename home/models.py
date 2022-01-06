from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=200, null=True, blank=True)
    countInStock = models.PositiveIntegerField(default=0) # Only positive integer is allowed
    image = models.ImageField(default='default.png', upload_to='product_pics')
    
    # This function sets how the post objects are displayed when being called.
    def __str__(self) -> str:
        return self.name
    