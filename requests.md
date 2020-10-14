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
res = requests.get("http://www.baidu.com/s",params=params)


``` 


    
  