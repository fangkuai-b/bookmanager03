from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('每次请求前都会调用执行')
        username = request.COOKIES.get('name')
        if username is None:
            print('无用户信息')
        else:
            print(username)

    def process_response(self, request, response):
        print('每次响应前都会调用执行')
        return response


class TestMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('每次请求前都会调用执行2')
        username = request.COOKIES.get('name')
        if username is None:
            print('无用户信息2')
        else:
            print(username)

    def process_response(self, request, response):
        print('每次响应前都会调用执行2')
        return response