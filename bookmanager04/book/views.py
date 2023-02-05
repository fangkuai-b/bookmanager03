from django.http import HttpResponse


def create_book(request):
    return HttpResponse("create sucess")