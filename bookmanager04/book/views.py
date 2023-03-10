import json

from django.http import HttpResponse, JsonResponse

from book.models import BookInfo


def create_book(request):
    book = BookInfo.objects.create(
        name='abc',
        pub_date='2022-02-05',
        readcount=1,
        commentcount=2
    )

    return HttpResponse("create sucess")


def goods(request, cat_id, mobile):
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
    print(data)  # <QueryDict: {'username': ['itcast'], 'password': ['123']}>
    return HttpResponse('OK')


def json_data(request):
    body = request.body
    print(body)  # b'{\r\n    "a": 1,\r\n    "b": "2b2",\r\n    "c": "c"\r\n}'
    body_str = body.decode()  # 可省略
    print(body_str)
    '''
    {
        "a": 1,
        "b": "2b2",
        "c": "c"
    }
    '''
    print(type(body_str))  # <class 'str'>
    req_data = json.loads(body_str)
    print(req_data)  # {'a': 1, 'b': '2b2', 'c': 'c'}
    print(req_data['a'])  # 1
    print(req_data['b'])  # 2b2
    print(req_data['c'])  # c

    print(
        request.META)  # {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\fangkuaib\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': '方块B', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'CONFIGSETROOT': 'C:\\Windows\\ConfigSetRoot', 'DJANGO_SETTINGS_MODULE': 'bookmanager04.settings', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\fangkuaib', 'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\fangkuaib\\Desktop', 'LOCALAPPDATA': 'C:\\Users\\fangkuaib\\AppData\\Local', 'LOGONSERVER': '\\\\方块B', 'NUMBER_OF_PROCESSORS': '24', 'ONEDRIVE': 'C:\\Users\\fangkuaib\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'D:\\software\\VMware\\bin\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\Windows\\RCC-Interface;D:\\software\\Git\\cmd;D:\\software\\mysql-8.0.32-winx64\\mysql-8.0.32-winx64\\bin;C:\\Users\\fangkuaib\\AppData\\Local\\Programs\\Python\\Python39;C:\\Users\\fangkuaib\\AppData\\Local\\Programs\\Python\\Python39\\Scripts;C:\\Users\\fangkuaib\\AppData\\Local\\Microsoft\\WindowsApps;D:\\software\\pycharm\\PyCharm 2022.3.1\\bin;;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 183 Stepping 1, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': 'b701', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM': 'D:\\software\\pycharm\\PyCharm 2022.3.1\\bin;', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'GBK', 'PYTHONPATH': 'F:\\fangkuaib_wwsyDDUP\\Python\\Django\\Django_project\\bookmanager04;D:/software/pycharm/PyCharm 2022.3.1/plugins/python/helpers/pycharm_matplotlib_backend;D:/software/pycharm/PyCharm 2022.3.1/plugins/python/helpers/pycharm_display', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\FANGKU~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\FANGKU~1\\AppData\\Local\\Temp', 'USERDOMAIN': '方块B', 'USERDOMAIN_ROAMINGPROFILE': '方块B', 'USERNAME': 'fangkuaib', 'USERPROFILE': 'C:\\Users\\fangkuaib', 'WINDIR': 'C:\\Windows', 'ZES_ENABLE_SYSMAN': '1', 'RUN_MAIN': 'true', 'SERVER_NAME': '方块B', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '48', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/json_data/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'application/json', 'HTTP_USER_AGENT': 'PostmanRuntime/7.30.0', 'HTTP_ACCEPT': '*/*', 'HTTP_POSTMAN_TOKEN': '00ec442e-b86c-4b6c-aa75-9fa5fca59cd4', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_CONNECTION': 'keep-alive', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x0000029B8BFD2E20>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='gbk'>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>}
    print(request.META['SERVER_PORT'])  # 8000
    return HttpResponse('json')


def method(request):
    method = request.method
    print(method)  # POST
    user = request.user
    print(user)  # AnonymousUser
    path = request.path
    print(path)  # /method/
    encoding = request.encoding
    print(encoding)  # None
    return HttpResponse('Method')


def response(request):
    # return HttpResponse('res',status=666) HTTP status code must be an integer from 100 to 599.
    # 1xx   消息
    # 2xx   成功
    # 3xx   重定向
    # 4xx   请求端问题
    #     404 路由问题，不存在，
    #     403 权限问题，禁止访问
    # 5xx   服务端问题
    response = HttpResponse('res', status=200)
    response['name'] = 'fangkuaib'
    return response


def json_response(request):
    # json-->dict
    # dict-->json
    info = {'city': 'beijing', 'subject': 'python'}
    response = JsonResponse(data=info)

    info_2 = [{'city': 'beijing', 'subject': 'python'}, {'city': 'beijing', 'subject': 'python'}]
    # response_2 = JsonResponse(data=info_2)    In order to allow non-dict objects to be serialized set the safe parameter to False.
    response_2 = JsonResponse(data=info_2, safe=False)  # safe如果为true表示data是字典数据，如果是非字典数据，JsonResponse可以转换为json，出问题自己负责
    return response_2

    # 重定向 redirect
    # from django.shortcuts import redirect
    # return redirect('http://www.baidu.com')


'''
第一次请求，携带查询字符串
http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
服务器收到请求之后获取username，服务器设置cookie信息，cookie信息包括username
浏览器收到服务器的响应之后，应该吧cookie保存起来。

第二次及其之后的请求，我们访问http://127.0.0.1:8000/时都会携带cookie信息。服务器就可以读取cookie信息来判断用户身份；
'''


def set_cookie(request):
    # 1.获取字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2.服务器设置cookie信息
    # 通过相应对象的set_cookie()方法
    response = HttpResponse('set_cookie')
    response.set_cookie('name', username)  # 不设置则默认关闭浏览器删除cookie
    response.set_cookie('pwd', password, max_age=3600)  # 过期时间一小时

    return response


def get_cookie(request):
    # 获取cookie
    cookie = request.COOKIES
    print(cookie)  # {'name': 'itcast'}
    name = cookie.get('name')
    return HttpResponse(name)


def del_cookie(request):
    # 删除cookie
    response = HttpResponse('删除cookie成功')
    response.delete_cookie('pwd')
    return response


'''
session是保存在服务器端的（默认保存到数据库中），数据是相对安全的
session需要依赖于cookie

第一次请求 http://127.0.0.1:8000/set_session/?username=fangkuaib 我们在服务器端设置session信息
服务器端同时会生成一个sessionid的cookie信息。
浏览器接收到信息之后会把cookie数据保存起来

第二次及其之后的请求都会携带这个sessionid，服务器会验证这个sessionid。
验证没问题会读取相关数据，实现业务逻辑
'''


def set_session(request):
    # 1.模拟获取用户信息
    username = request.GET.get('username')
    # 2.设置session信息
    # 假如我们通过模型查询到了用户的session信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    # 设置session的过期时间,如果不设置，则默认两周
    request.session.set_expiry(7200)
    # clear 删除session里的数据，但是key有保留
    # request.session.clear()
    # flush 是删除所有的数据，包括key
    # request.session.flush()
    return HttpResponse('set session')


def get_session(request):
    session_id = request.COOKIES.get('sessionid')
    print(session_id)  # csi9pjn22apd4su2rv78k3ipyann3e0o
    # user_id = request.session['user_id']
    # user_name = request.session['username']
    user_id = request.session.get('user_id')  # 用get可以避免报错，get获取不存在返回None
    user_name = request.session.get('username')
    content = '{},{}'.format(user_id, user_name)
    print(user_id)  # 1
    print(user_name)  # fangkuaib
    return HttpResponse(content)  # 返回1,fangkuaib


def login(requset):
    '''类视图'''
    print(requset.method)
    if requset.method == 'GET':
        return HttpResponse('get 逻辑')
    elif requset.method == 'POST':
        return HttpResponse('POST 逻辑')
    else:
        return HttpResponse('请求方式错误！！！')


'''
类视图定义

class 类视图名字(view)：
    def get(self, request):
        return HttpResponse('xxx')
    def http_method_lower(self, request):
        return HttpResponse('xxx')

1、继承自View
2、类视图中的方法 是采用 http方法小写来区分不同的请求方式的
'''
from django.views import View


class LoginView(View):
    def get(self, request):
        return HttpResponse('get it')

    def post(self, request):
        return HttpResponse('post post post')


class Person(object):
    # 对象方法
    def play(self):
        pass

    # 类方法
    @classmethod
    def say(cls):
        pass

    # 静态方法
    @staticmethod
    def eat():
        pass


Person.say()
cls = Person
Person()
cls()

'''
我的订单、个人中心页面
如果登录用户 可以访问
如果未登录用户 不应该访问，应该跳转到登录页面

定义一个订单，个人中心 类视图
判断我有没有登录？？？以登录有没有登录后台站点为例。
'''

from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin 判断只有登录用户才可以访问页面
# LoginRequiredMixin 内部会进行用户是否登录的判断，以登录admin判断，如果登录成功，则显示页面，如果未登录则跳转到以下/accounts/login/页面。
'''
多继承 python c++
继承了多个父类。
调用顺序遵循MRO顺序
'''


# class OrderView(View, LoginRequiredMixin):
class OrderView(LoginRequiredMixin, View):
    def get(self, request):
        # 标记位
        # isLogin = True
        # if not isLogin:
        #     return HttpResponse('没有登录，跳转到登录页面')
        return HttpResponse(
            '我的订单页面，这个页面必须登录。')  # 没登录则跳转到http://127.0.0.1:8000/accounts/login/?next=/order/

    def post(self, request):
        return HttpResponse('POST')
