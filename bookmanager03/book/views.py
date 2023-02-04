from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo, PeopleInfo
from django.db.models import F, Q, Sum, Max, Min, Avg, Count
from django.core.paginator import Paginator # 分页

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

'''
# 聚合函数和排序函数
# 1. 聚合函数
# 使用aggregate()过滤器调用聚合函数。聚合函数包括：Avg平均，Count数量，Max最大，Min最小，Sum求和，被定义在django.db.models中。
from django.db.models import F, Q, Sum, Max, Min, Avg, Count

# 查询图书的总阅读量。
BookInfo.objects.aggregate(Sum('read_count'))  # {'read_count__sum': 249}
# 查询图书总数。
BookInfo.objects.count()  # 6
# 2. 排序
# 使用order_by对结果进行排序,默认升序，降序在前面加-
BookInfo.objects.all().order_by('read_count')
BookInfo.objects.all().order_by('-read_count')
'''

'''
# 级联查询
# 关联查询
# 查询书籍为1的所有人物信息（由一到多）
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()
# 查询人物为1的书籍信息（由多到一）
people = PeopleInfo.objects.get(id=18)
people.book
people.book.name

# 关联过滤查询
# 由多模型类条件查询-模型类数据:
# 语法如下：
# 模型类名.objects.关联模型类名小写__属性名__条件运算符=值
# 注意：如果没有"__运算符"部分，表示等于。
# 查询图书，要求图书人物为"郭靖"
book = BookInfo.objects.filter(peopleinfo__name='郭靖')
book = BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
book
# 查询图书，要求图书中人物的描述包含"八"
book = BookInfo.objects.filter(peopleinfo__description__contains='八')

# 由一模型条件查询多模型类数据:
# 语法如下：
# 一模型类关联属性名__一模型类属性名__条件运算符=值
# 注意：如果没有"__运算符"部分，表示等于。
# 查询书名为“天龙八部”的所有人物
people = PeopleInfo.objects.filter(book__name='天龙八部')
people = PeopleInfo.objects.filter(book__name__exact='天龙八部')
# 查询图书阅读量大于30的所有人物
people = PeopleInfo.objects.filter(book__read_count__gt=30)
'''

'''
# 两大特性
# 2.1惰性执行
# 创建查询集不会访问数据库，直到调用数据时，才会访问数据库，调用数据的情况包括迭代、序列化、与if合用
# 例如，当执行如下语句时，并未进行数据库查询，只是创建了一个查询集books
books = BookInfo.objects.all()
# 继续执行遍历迭代操作后，才真正的进行了数据库的查询
for book in books:
    print(book.name)

# 2.2缓存
# 使用同一个查询集，第一次使用时会发生数据库的查询，然后Django会把结果缓存下来，再次使用这个查询集时会使用缓存的数据，减少了数据库的查询次数。
# 情况一：如下是两个查询集，无法重用缓存，每次查询都会与数据库进行一次交互，增加了数据库的负载。
from book.models import BookInfo
[book.id for book in BookInfo.objects.all()]
[book.id for book in BookInfo.objects.all()
# 情况二：经过存储后，可以重用查询集，第二次使用缓存中的数据。
books=BookInfo.objects.all()
[book.id for book in books]
[book.id for book in books]
'''

'''
books = BookInfo.objects.all()[0:2]
'''

'''
>>> from django.core.paginator import Paginator
>>> books = BookInfo.objects.all()
>>> p = Paginator(books, 2)   
<console>:1: UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'book.models.BookInfo'> QuerySet.
>>> p
<django.core.paginator.Paginator object at 0x00000281E82747F0>
>>> p.count()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'int' object is not callable
>>> p.count  
6
>>> p.num_pages
3
>>> type(p.page_range)
<class 'range'>
>>> p.page_range
range(1, 4)
>>> page1 = p.page(1)
>>> page1
<Page 1 of 3>
>>> page1.object_list
<QuerySet [<BookInfo: 射雕英雄传>, <BookInfo: 天龙八部>]>
>>> page2 = p.page(2) 
>>> page2             
<Page 2 of 3>
>>> page2.object_list 
<QuerySet [<BookInfo: 笑傲江湖>, <BookInfo: 雪山飞狐>]>
>>> page3 = p.page(3) 
>>> page3             
<Page 3 of 3>
>>> page3.object_list 
<QuerySet [<BookInfo: 运维开发入门>, <BookInfo: Django入门>]>
>>> page3.has_next() 
False
>>> page3.has_previous() 
True
>>> page1.has_previous() 
False
>>> page3.has_other_pages()   
True
>>> page3.next_page_number()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\fangkuaib\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\paginator.py", line 171, in next_page_number
    return self.paginator.validate_number(self.number + 1)
  File "C:\Users\fangkuaib\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\paginator.py", line 52, in validate_number
    raise EmptyPage(_('That page contains no results'))
django.core.paginator.EmptyPage: 本页结果为空
>>> page3.previous_page_number()
2
>>> page3.start_index() 
5
>>> page3.end_index()   
6
>>> p.page(0)          
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\fangkuaib\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\paginator.py", line 70, in page
    number = self.validate_number(number)
  File "C:\Users\fangkuaib\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\paginator.py", line 47, in validate_number
    raise EmptyPage(_('That page number is less than 1'))
django.core.paginator.EmptyPage: 页码小于 1
>>> p.page(4) 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\fangkuaib\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\paginator.py", line 70, in page
    number = self.validate_number(number)
  File "C:\Users\fangkuaib\AppData\Local\Programs\Python\Python39\lib\site-packages\django\core\paginator.py", line 52, in validate_number
    raise EmptyPage(_('That page contains no results'))
django.core.paginator.EmptyPage: 本页结果为空

'''