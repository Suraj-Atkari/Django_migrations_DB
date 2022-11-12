from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("/book_details", views.book_details)
]
