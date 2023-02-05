from django.urls import path
from book.views import create_book, goods, register, json_data, method

urlpatterns = (
    path('create_book/', create_book),
    # <转换器名字：变量名>
    # 转换器会对变量名进行正则的验证
    path('<int:cat_id>/<int:id>/', goods),
    path('register/', register),
    path('json_data/', json_data),
    path('method/', method)
)
