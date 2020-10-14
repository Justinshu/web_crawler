# requests库
> 虽然Python的标准库中 urllib模块已经包含了平常我们使用的大多数功能，
> 但是它的 API 使用起来让人感觉不太好，而 Requests宣传是 “HTTP for Humans”，说明使用更简洁方便。

# 安装和文档地址

## 利用pip 工具可以安装
> pip install requests

> 如果比较慢的话可以尝试：pip install requests -i https://pypi.douban.com/simple

## 文档
* 中文文档：[http://docs.python-requests.org/zh_CN/latest/index.html](http://docs.python-requests.org/zh_CN/latest/index.html)
* 英文文档：[https://github.com/requests/requests](https://github.com/requests/requests)

# 发送GET请求

1.最简单的发送`get`请求是通过`request.get()`来调用的
  * response = requests.get("http://www.baidu.com/")

2.添加headers参数和查询参数：
  * 如果想添加headers，可以传入headers参数来增加请求头中的headers信息，如果要将参数放在url中传递，可以利用params参数，相关的实例代码如下;
```python

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

params = {
    "wd":"中国",
}

# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s",params=params)

# 查看响应的内容，response.text返回的是Unicode格式数据,会自动识别编码格式，但是会出现识别出错问题
print(response.text)

# with open("baidu.html","w",encoding="utf-8") as f:
#     f.write(response.text)

# 查看响应的内容，response.content返回的是字节流数据，可以自行进行的解码，指定解码格式
print(response.content)
# with open("baidu.html","w",encoding="utf-8") as f:
#     f.write(response.content.decode("utf-8"))

# 查看完整的url地址
print(response.url)

# 查看响应的头部信息的字符串编码格式
print(response.encoding)

# 查看响应码
print(response.status_code)

``` 

# 发送POST请求

1.最基本的POST请求可以使用post方法：
response = requests.post(url ,data=data)

2.传入data数据：这时候就不要再使用urlencode进行编码了，直接传入一个字典进去就可以了。比如请求拉勾网的数据的代码：
```python
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0"

headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
 'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
}

data = {
 'first': 'true',
 'pn': 1,
 'kd': 'python'
}

resp = requests.post(url,headers=headers,data=data)
# 如果是json数据，直接可以调用json方法,或者导入json库进行load操作
print(resp.json())

```
# 使用代理
> 使用requests添加代理也非常简单，只要在请求的方法中（比如get或者post）传递proxies参数就可以了。示例代码如下：

```python
import requests

url = "http://httpbin.org/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

proxy = {
    'http': '114.220.15.125:57114'
}

resp = requests.get(url,headers=headers,proxies=proxy)
with open('xx.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)
```
# cookie
> 如果在一个响应中包含了cookie，那么可以利用cookies属性拿到这个返回的cookie值

```python
import requests

url = "http://www.renren.com/PLogin.do"

data = {
    "email":"你的邮箱",
    'password':"你的密码"
    }
    
resp = requests.get(url)
print(resp.cookies)
# 将cookie信息存储成一个字典的形式
print(resp.cookies.get_dict())
```
# session(会话)

> 之前使用urllib库，是可以使用opener发送多个请求，多个请求之间是可以共享cookie的。
> 那么如果使用requests，也要达到共享cookie的目的，那么可以使用requests库给我们提供的session对象。注意，这里的session不是web开发中的那个session，这个地方只是一个会话的对象而已。还是以登录人人网为例，使用requests来实现。示例代码如下：

```python
import requests

url = "http://www.renren.com/PLogin.do"
data = {
    "email":"你的邮箱",
    'password':"你的密码"
    }
    
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}

# 登录
session = requests.session()
session.post(url,data=data,headers=headers)

# 访问大鹏个人中心
resp = session.get('http://www.renren.com/880151247/profile')

print(resp.text)
```

# 处理不信任的SSL证书：

> 对于那些已经被信任的SSL证书的网站，比如https://www.baidu.com/，那么使用requests直接就可以正常的返回响应。示例代码如下：
```python
import requests
resp = requests.get('http://www.12306.cn/mormhweb/',verify=False)
print(resp.content.decode('utf-8'))
```
