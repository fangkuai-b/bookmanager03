import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

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


from django.http import HttpResponseNotFound


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