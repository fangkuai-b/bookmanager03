from django.urls import path
from book.views import create_book, goods

urlpatterns = (
    path('create_book/', create_book),
    path('<cat_id>/<id>/', goods),
)
