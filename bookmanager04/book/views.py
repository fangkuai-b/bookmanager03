from django.http import HttpResponse
from book.models import BookInfo


def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2022-02-05',
        readcount=1,
        commentcount=2
    )

    return HttpResponse("create sucess")


def goods(request, cat_id, id):
    query_parmas = request.GET
    print(
        query_parmas)  # http://127.0.0.1:8000/101/10055/?order=desc  返回打印结果：<QueryDict: {'a': ['1', '3'], 'b': ['2']}>
    a = query_parmas.get('a')
    b = query_parmas['b']
    a_list = query_parmas.getlist('a')
    print(a)  # 3
    print(b)  # 2
    print(a_list)  # ['1', '3']
    return HttpResponse('sucess ')


'''
查询字符串
http://ip:port/path/path/:?key1=value1&key2=value2
url 以 ? 分割为2部分
?之前的部分为请求路径
?之后的部分为查询字符串，类似于字典的key=value形式，多个数据采用&符拼接
'''


def register(request):
    data = request.POST
    print(data)
    return HttpResponse('OK')