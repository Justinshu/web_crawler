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
> 在你爬取一个网站的时候可以利用这个类设置浏览器的请求头，伪装浏览器运行，而不是直接使用urlopen让浏览器知道你是一个Python爬虫

```python
from urllib import request


request.Request(url= "",headers=)

request.urlopen()

```









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







