from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Content(models.Model):
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
