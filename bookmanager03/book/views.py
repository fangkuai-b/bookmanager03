from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo, PeopleInfo
from django.db.models import F, Q


# Create your views here.
def index(request):
    # 在这里实现 增删改查
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("index")


"""
##############################增加##################################
# 增加
# 方式一
book = BookInfo(
    name='python入门',
    pubdate='2023-01-04',
    read_count='123'
)
book.save()  # 必须调用对象.save方法；

# 方式二
BookInfo.objects.create(
    name='Django入门',
    pubdate='2012-01-23'
)

##############################修改##################################
# 修改
# 方式一
book = BookInfo.objects.get(id=12)
book.name = '运维开发入门'
book.save()

# 方式二
# filter 过滤
BookInfo.objects.filter(id=6).update(name='python 入门必备', comment_count='111')

##############################删除##################################
# 删除
# 方式一
# 物理删除
book = BookInfo.objects.get(id='6')
book.delete()
# 逻辑删除，即修改is_delete=False删除标记，同update

# 方式二
BookInfo.objects.get(id=7).delete()
BookInfo.objects.filter(id=5).delete()

##############################查询##################################
# 查询
# get   查询单一结果
book = BookInfo.objects.get(id=1)  # <BookInfo: 射雕英雄传>

# all   查询多个结果
books = BookInfo.objects.all()  # <QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>, <BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>]>

# get 查询单一结果，不存在则 raise self.model.DoesNotExist
try:
    book = BookInfo.objects.get(id=120)
except BookInfo.DoesNotExist:
    print('查询结果不存在')

# count 查询结果数量
BookInfo.objects.count()
BookInfo.objects.all().count()

##############################过滤查询##############################
'''
实现SQL中的where功能，包括
    filter过滤出多个结果
    exclude排除掉符合条件剩下的结果
    get过滤单一结果
对于过滤条件的使用，上述三个方法相同，故仅以filter进行讲解。
过滤条件的表达语法如下：
    属性名称__比较运算符=值
    如 id__exact=1 过滤表示id=1的数据
    属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线
        exact：表示判等。
        contains：是否包含。
        startswith、endswith：以指定值开头或结尾。
        isnull：是否为null。
        in：是否包含在范围内。
        比较查询
            gt大于 (greater then)
            gte大于等于 (greater then equal)
            lt小于 (less then)
            lte小于等于 (less then equal)
        不等于的运算符，使用exclude()过滤器。
        year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算。
'''

# 查询编号为1的图书
BookInfo.objects.get(id__exact=1)  # <BookInfo: 射雕英雄传>     get 得到的是一个
BookInfo.objects.filter(id__exact=1)  # <QuerySet [<BookInfo: 射雕英雄传>]>    filter 得到的是列表
BookInfo.objects.get(id=1)
BookInfo.objects.get(pk=1)  # pk 为primary key   主键

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1, 2, 5))

# 查询编号大于3的图书
# gt大于 (greater then)
# gte大于等于 (greater then equal)
# lt小于 (less then)
# lte小于等于 (less then equal)
BookInfo.objects.filter(id__gt='3')

# 查询编号不等于3的图书
BookInfo.objects.exclude(id__exact='3')

# 查询1980年发表的图书
BookInfo.objects.filter(pubdate__year='1980')

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pubdate__gt='1990-01-01')
"""


'''
# F对象和Q对象
# F对象
# 语法如下：
#     F(属性名)
from django.db.models import F
# 查询阅读量大于等于评论量的图书。
BookInfo.objects.filter(read_count__gt=F('comment_count'))    # <QuerySet [<BookInfo: 雪山飞狐>, <BookInfo: 运维开发入门>]>
# 查询阅读量大于2倍评论量的图书。
BookInfo.objects.filter(read_count__gt=F('comment_count')*2)

# 并且查询
# 查询阅读量大于20，并且编号小于3的图书。
# 方式1
BookInfo.objects.filter(read_count__gt=20, id__lt=3)
# 方式二 （多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字。）
BookInfo.objects.filter(read_count__gt=20).filter(id__lt=3)

或者查询or
# Q对象
from django.db.models import Q
# Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或。
# Q(属性名__运算符=值)
# 查询阅读量大于20的图书，改写为Q对象如下。
BookInfo.objects.filter(Q(read_count__gt=20))
# 查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
BookInfo.objects.filter(Q(read_count__gt=20)|Q(id__lt=3))
# Q对象前可以使用~操作符，表示非not。
# 查询编号不等于3的图书。
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))
'''