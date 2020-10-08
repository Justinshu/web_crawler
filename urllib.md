# urllib库
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

>方便将网页上面的一个文件保存到本地
```python
from urllib import request

request.urlretrieve("https://www.baidu.com","baidu.html")

```