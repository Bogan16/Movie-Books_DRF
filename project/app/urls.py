# from django.urls import path

# from . import views

# urlpatterns = [
#     path('movies/', views.movies),
#     path('movies/<int:movie_id>', views.movie),
#     # path('movies/<int:arg>', views.movie)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews),
    path('reviews/<int:review_id>/', views.review_detail),
    path('books/', views.books),  # Новый URL для представления книг
    path('books/<int:book_id>/', views.book_detail),  # Новый URL для конкретной книги
    path('movies/', views.movies),
    path('movies/<int:movie_id>/', views.movie),
]