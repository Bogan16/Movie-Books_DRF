from rest_framework import serializers

from . import models

from .models import Review, Book



class SerializedMovie(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['title', 'raitng', 'description', 'slug']


class SerializedTicket(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ['movie', 'price']


class SerializedPlace(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ['amount', 'owner']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'text', 'date']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'rating', 'desc', 'slug']