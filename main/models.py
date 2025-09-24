from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    PRODUCT_CHOICES = [
        ("shoes", "Shoes"),
        ("ball", "Ball"),
        ("shin guards", "Shin Guards"),
        ("jersey", "Jersey"),
        ("shorts", "Shorts"),
        ("socks", "Socks"),
        ("goalkeeper gloves", "Goalkeeper Gloves"),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=30, choices=PRODUCT_CHOICES,
                                default="shoes")
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name