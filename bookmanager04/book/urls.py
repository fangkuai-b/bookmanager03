from django.urls import path
from book.views import create_book, goods, register, json_data

urlpatterns = (
    path('create_book/', create_book),
    path('<cat_id>/<id>/', goods),
    path('register/', register),
    path('json_data/', json_data)
)
