from django.urls import path, include
from . import views

urlpatterns = [
    path("books/", views.create_book),
    path("users/", views.create_user),
    path("borrows/", views.borrow_books),
    path("users/<int:id>/borrowed", views.borrow_list)
]
