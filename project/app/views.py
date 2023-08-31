from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Review, Book
from .serializers import ReviewSerializer, BookSerializer
from . import serializers
from . import models


class HomeView(APIView):
    
    def get(self, request):
        data = {
            "message": "Welcome to the book viewer!",
        }
        return Response(data)

@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def get_data(amount, req, outer_model, outer_serializer):
    match(amount):
        case 'singular':
            model = outer_model

            serialized_model = outer_serializer(model)

            serialized_model_data = serialized_model.data

            return Response(serialized_model_data, status=status.HTTP_200_OK)

        case 'plural':
            model = outer_model

            serialized_model = outer_serializer(model, many=True)

            serialized_model_data = serialized_model.data

            return Response(serialized_model_data, status=status.HTTP_200_OK)

        case _:
            return Response({"msg": "Something went wrong!"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movies(req):
    if req.method == "GET":
        return get_data(
            'plural',
            req,
            models.Movie.objects.all(),
            serializers.SerializedMovie
        )

    if req.method == "POST":
        models.Movie.objects.create(**req.data)

        return Response(serializers.SerializedMovie(models.Movie.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def movie(req, movie_id):
    if req.method == "GET":
        return get_data(
            'singular',
            req,
            models.Movie.objects.get(id=movie_id),
            serializers.SerializedMovie
        )

    if req.method == "PUT":
        old_model = models.Movie.objects.get(id=movie_id)

        updated_item = serializers.SerializedMovie(
            old_model, data=req.data, partial=False)

        updated_item.is_valid(raise_exception=True)
        updated_item.save()

        return Response(serializers.SerializedMovie(models.Movie.objects.all(), many=True).data)

    if req.method == "DELETE":
        old_model = models.Movie.objects.get(id=movie_id)

        old_model.delete()

        return Response(serializers.SerializedMovie(models.Movie.objects.all(), many=True).data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def customers(req):
    pass


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def customer(req):
    pass
