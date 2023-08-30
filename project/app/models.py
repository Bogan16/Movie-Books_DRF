from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    desc = models.TextField()
    slug = models.SlugField()

class Movie(models.Model):
    title = models.CharField(max_length=23)
    raitng = models.FloatField()
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self) -> str:
        return f"{self.title} : {self.raitng}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Ticket(models.Model):
    movie = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.FloatField()


class Place(models.Model):
    amount = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE)