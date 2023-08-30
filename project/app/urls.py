from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews),
    path('reviews/<int:review_id>/', views.review_detail),
    path('books/', views.books),
    path('books/<int:book_id>/', views.book_detail),
    path('movies/', views.movies),
    path('movies/<int:movie_id>/', views.movie),
]