from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message[:30]}"