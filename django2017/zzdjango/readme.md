环境：win7、python3.6.3、django2.0

# django 学习笔记

#### 例如： 创建项目 zzdjango，创建应用blog

django-admin  startproject   zzdjango　　创建项目

cd  zzdjango

tree -f　　（windows下看一下目录结构）

python manage.py   startapp  blog　　创建应用

tree -f　　（再看一下，已出现应用：blog）



```
│  db.sqlite3
│  manage.py  # 管理项目：包括数据库建立、服务器运行、测试（manage.py是个大管家，做什么事情都要找它）
│
├─blog        # （项目目录。 django中使用应用来分隔功能）
│  │  admin.py   # admin相关
│  │  apps.py    # 当前应用的一些配置（django1.9以后自动生成）
│  │  models.py  # 定义数据库中的表
│  │  tests.py   # 测试相关
│  │  views.py   # 响应用户请求，返回html页面
│  │  __init__.py
│  │
│  └─migrations
│          __init__.py
│
└─zzdjango        # （工程目录）
    │  settings.py  # 配置文件：应用、中间件、数据库、静态目录
    │  urls.py      # URL映射配置文件：决定一个url访问被哪个程序
    │  wsgi.py      # python应用程序或框架和Web服务器之间接口（目前用不到。以后要放在公网用nginx了，再做配置）----WSGI(Python Web Server Gateway Interface)python服务器网关接口
    │  __init__.py
    │
    └─__pycache__
            settings.cpython-36.pyc
            urls.cpython-36.pyc
            wsgi.cpython-36.pyc
            __init__.cpython-36.pyc
```

### 创建应用后，需要把应用添加进去。  

```
#settings.py 的 40行，添加  blog

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```
另外，settings.py的 26 行：　　DEBUG = True　　这是打开debug的开关

凡是和wsgi有关的都不用动它。


### 运行django 服务

python manage.py runserver　　运行django 服务http://localhost:8000/

或：python manage.py runserver  8080　　　　http://localhost:8080/

或：python manage.py runserver 0.0.0.0:8080　　　　http://0.0.0.0:8080/

python manage.py  shell　　　　进入SHELL

python manage.py　　查看有哪些命令（最常用的：runserver启动服务器；migrate makemigrations做好一个model后用这两条更新数据库表；shell。这4条命令是最常用的）


### 配置URL：
#### 第一种配置URL：

C:\Python3\zzdjango\zzdjango\urls.py 此文件配置以下内容：

```
import blog.views as bv        # 可是为什么要这样写呢？ 如果是z直接import blog，后面写 urlpatterns 怎么弄都不行。
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', bv.helloworld),    # 要这样写
    #url(r'blog/',bv.helloworld),    # 这样写也行
]
```

C:\Python3\zzdjango\blog\views.py 此文件加入以下内容：

```
from django.shortcuts import render
from django.http import HttpResponse
def helloworld(request):
    return HttpResponse('<html>hello111</html>')
```

#### 第二种配置URL：

在根url.py中引入include

在APP目录下创建urls.py文件，各式与根urls.py相同

根urls.py中url函数第二个参数改为 include('blog.urls')

C:\Python3\zzdjango\zzdjango\urls.py　　根urls配置如下：

```
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'blog/', include('blog.urls')),
]
```
C:\Python3\zzdjango\blog\urls.py　　blog应用的urls配置如下：

```
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',views.index),        # 第一个参数是正则，所以用^开头，用$结尾，约束为是一个空字符串
    url(r'^hello/$',views.hello),     # 这里要注意一定要有 /
]
```

### http://localhost:8000/blog/
### http://localhost:8000/blog/hello/