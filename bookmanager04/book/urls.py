from django.urls import path, converters
from django.urls.converters import register_converter
from book.views import create_book, goods, register, json_data, method, response, json_response
from book.views import set_cookie, get_cookie, del_cookie
from book.views import set_session, get_session
from book.views import login, LoginView, OrderView


# 1、定义转换器
class MobileConverter:
    # 重写验证数据的的正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据给视图函数
    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        # 反向解析传值时使用
        return str(value)


# 2、注册转换器,才能在下一步使用 register_converter(converter, type_name):
register_converter(MobileConverter, 'phone')
# 3、使用


urlpatterns = (
    path('create_book/', create_book),
    # <转换器名字：变量名>
    # 转换器会对变量名进行正则的验证
    path('<int:cat_id>/<phone:mobile>/', goods),
    path('register/', register),
    path('json_data/', json_data),
    path('method/', method),
    path('res/', response),
    path('json_response/', json_response),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('del_cookie/', del_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
    path('login/', login),
    path('163_login/', LoginView.as_view()),
    path('order/', OrderView.as_view()),
)
