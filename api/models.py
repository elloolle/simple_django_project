from abc import ABC, abstractmethod

from django.db import models

from django.contrib.auth.models import AbstractUser

# class Recipe(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name
class User(AbstractUser):
    pass

class Content(models.Model, ABC):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "pending"),
            ("approved", "approved"),
            ("rejected", "rejected"),
        ],
        default="pending",
    )

    class Meta:
        abstract = True


class Text(Content):
    author = models.ForeignKey(User, related_name="texts", on_delete=models.CASCADE)
    text = models.TextField()


class Image(Content):
    author = models.ForeignKey(User, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")


class Video(Content):
    author = models.ForeignKey(User, related_name="videos", on_delete=models.CASCADE)
    video = models.FileField(upload_to="videos/")
