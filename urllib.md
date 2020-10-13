# urllib库中的parse

> 使用urllib库中的parse可以解析和编码数据

## urlencode 编码
> 对于底层ASCII码无法识别的中文字体进行编码

```python
from urllib import parse
params = {
    "name": "张三" ,
    "age" : 18,
    "sex" : "male"
    }

result = parse.urlencode(params)

print(result)

# name=%E5%BC%A0%E4%B8%89&age=18&sex=male
```

## parse_qs 解码
> 对于编码后的数据进行解码

```python
from urllib import parse
date = {
    "name": "张三" ,
    "age" : 18,
    "sex" : "male"
    }

qs = parse.urlencode(date)
print(qs)

result = parse.parse_qs(qs)
print(result)

# name=%E5%BC%A0%E4%B8%89&age=18&sex=male
# {'name': ['张三'], 'age': ['18'], 'sex': ['male']}

```

## urlparse和urlsplit 
> 用来解析url每一个参数，从而获取到每个参数的值，区别是urlparse中多了一个params参数

```python
from urllib import parse

url = "https://www.baidu.com/s;hello word?wd=hello word&username=123#date"

result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)

print(result1)
print(result2)

# ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='hello word', query='wd=hello word&username=123', fragment='date')
# SplitResult(scheme='https', netloc='www.baidu.com', path='/s;hello word', query='wd=hello word&username=123', fragment='date')


print("scheme：",result1.scheme)
print("netloc：",result1.netloc)
print("path：",result1.path)
print("params：",result1.params)
print("query：",result1.query)
print("fragment：",result1.fragment)

# scheme： https
# netloc： www.baidu.com
# path： /s
# params： hello word
# query： wd=hello word&username=123
# fragment： date


print("scheme：",result2.scheme)
print("netloc：",result2.netloc)
print("path：",result2.path)
print("query：",result2.query)
print("fragment：",result2.fragment)

# scheme： https
# netloc： www.baidu.com
# path： /s;hello word
# query： wd=hello word&username=123
# fragment： date

```

# urllib库中的request
>在`python3`的`urllib`库中，所有和网络请求相关的方法都被集成到`urllib.request`模块下面

## urlopen
> def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            *, cafile=None, capath=None, cadefault=False, context=None):

```Python
from urllib import request

response = request.urlopen("https://www.baidu.com")

# 返回值是一个http.client.HTTPResponse object
print(response)

# 类文件句柄被全部读取出来，可以设置读取多少个字  print(response.read(size = number))
print(response.read())

# 读取一行数据，也就是第一行数据
print(response.readline())

# 读取所有数据分成多行，返回的是一个列表
print(response.readlines())

# 响应码
print(response.getcode())

```

* `url`:请求的url
* `date`:请求的`date`，如果设置这个值，那么将变成`post`请求
* 返回值: 返回值是一个`<http.client.HTTPResponse object at 0x000002CE5BC12908>`,这个对象是一个类文件句柄对象，有`read(size)`、`readline`、`readlines`、`getcode`等方法

## urlretrieve
> def urlretrieve(url, filename=None, reporthook=None, data=None):

> 方便将网页上面的一个文件保存到本地
```python
from urllib import request

# url = 想要获取的网址      filename = 代表是下载好的文件文件位置和文件名称
request.urlretrieve("https://www.baidu.com","baidu.html")
# 下载铠爹的一张图片
request.urlretrieve("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1602244848418&di=55f89cc9014c7439c658df9539cdd59d&imgtype=0&src=http%3A%2F%2F01imgmini.eastday.com%2Fmobile%2F20200210%2F20200210124632_dce5fc05ecccb056da40c72aa8c0fe52_1.jpeg","urllib库/kai.png")

```

## request.Request类
> 在你爬取一个网站的时候可以利用这个类设置浏览器的请求头，伪装浏览器运行，而不是直接使用`urlopen`让浏览器知道你是一个`Python`爬虫
> 以拉勾网为例，获取`ajax`中的数据，过程稍微复杂，用到获取`session`或`cookie`来进行再次的询问
```python

import http.cookiejar
from urllib import request,parse
import time

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"

# 构造请求的数据 

form = {
    "first": "true",
    "pn": 1,
    "kd": "Python"
}

# 构造请求的头

headers = {
    "origin": "https://www.lagou.com",
    "referer": "https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

# 构造存储cookie和session的模型
cookie = http.cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

# 首次请求获取refer中get url后的cookie和session
resp = request.Request(url='https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=', headers=headers)
response = opener.open(resp,data=parse.urlencode(form).encode("utf-8"))

time.sleep(5)

# 再次使用上次获取的带有session和cookie的模型去post请求，这样服务器就准确识别，给到正确的数据
resp = request.Request(url, headers=headers)
response1 = opener.open(resp,data=parse.urlencode(form).encode("utf-8"))

# 普通的获取打开url后的结果，如果网站做了ajax中有cookie和session限制，就没办法用普通的方法来获取
# result= request.urlopen(resp,timeout=5)

print(response1.read().decode("utf-8"))

```
## ProxyHandler 处理器（代理设置）
> 设置代理的目的是防止服务器对于请求多次后，把自己的IP地址封掉，更换ip进行多次的访问
```python
from urllib import request

# 没有使用代理的访问

# res = request.urlopen("http://httpbin.org/get")
# print(res.read().decode("utf-8"))

# 这个是使用了代理的访问
handler = request.ProxyHandler({"http":"ip:端口号"})

opener = request.build_opener(handler)

res = request.Request("http://httpbin.org/ip")
resp = opener.open(res)

print(resp.read().decode("utf-8"))

```
常用的代理有
  * 西刺代理：[http://xicidaili.com/](http://xicidaili.com/)
  * 快代理：[http://kuaidaili.com/](http://kuaidaili.com/)
  * 代理云：[http://dailiyun.com/](http://dailiyun.com/)



## cookie的解释
在网站的开发中，`http`请求是无状态的请求，同一个用户发送两次请求他是不知道的是同一个用户发出的请求
`cookie`的出现就是为了解决这个问题，第一次登陆之后服务器返回一些数据（`cookie`）给浏览器，
然后浏览器保存在本地，当用户第二次发送请求的时候，就会自动的把上次请求存储的`cookie`数据自动携带给服务器，
服务器通过浏览器携带的数据就可以知道当前用户是哪一个了，`cookie`存储的数据有限，不同的浏览器有不同的存储大小，
但是一般不会超过4KB，因此使用`cookie`只能存储一些少量的数据


### cookie的格式
> Set-Cookie:NAME=VALUE; Expires/Max-age=DATE;Path=PATH;Domain=DOMAIN_NAME;SECURE

#### 参数意义:
  * NAME：cookie的名字
  * VALUE：cookie的值
  * Expires：cookie的过期时间
  * Path：cookie作用的路径
  * Domain：cookie作用的域名
  * SECURE：是否只是在https协议下起作用


### 使用cookielib库和HTTPCookieProcessor模拟登陆
`cookie`是指网站为了识别用户和进行`session`跟踪，而存储在用户本地的浏览器上的文本文件，
`cookie`可以保持登陆信息到下次用户登录与服务器进行会话
在这里以人人网站为例子，人人网中要访问某个主页，必须先登录才能进行访问，那就必须要有`cookie`信息
解决的方案有两种，一种是使用浏览器访问然后将`cookie`信息复制下来，放在`headers`中，如：
```python
from urllib import request

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "cookie":"浏览器复制的cookie值",
}

res = request.Request(url = "",headers=headers)
result = request.urlopen(res)
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(result.read().decode("utf-8"))

```

但是在每次在访问需要`cookie`的界面都需要手动的去浏览器中复制`cookie`值，比较麻烦，在`Python`处理`cookie`的时候
一般是通过`http.cookiejar`模块和`urllib`模块中的`HTTPCookieProcessor`处理器类一起使用，`http.cookiejar`模块
主要的作用是提供用于存储`cookie`的对象，而`HTTPCookieProcessor`处理器主要作用是处理这些`cookie`对象，并都贱`handler`对象