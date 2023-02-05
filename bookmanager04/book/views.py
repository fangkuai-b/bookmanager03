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
    return HttpResponse('sucess ')
