# xpath语法和lxml模块

> xpath(XML PATH LANGUAGE)是一门在xml和html中查找信息的语言，可以用来在xml和html文档中对元素和属性进行遍历

## xpath开发工具

* chrome插件： xpath helper

* Firefox插件： xpath checker


## xpath语法
### 详细语法

   * [点击可以转到对应链接](https://www.runoob.com/xpath/xpath-syntax.html)

### 常用方法

   * 使用//获取整个页面中的元素，然后写标签名，然后再写谓语进行提取，比如：

```xpath
//div[@class = "abc"]
```

### 需要注意的知识点

   * /和//的区别：/代表只获取直接子节点，//代表获取子孙节点，一般//用的比较多，当然也要视情况而定

   * `contains`：有时候某个属性中包含了多个值，那么可以使用`contains`函数，示例代码如下：
```xpath
//div[contains(@class,"jb_detail")]
```

   * 谓语中的下标是从1开始的，不是从0开始的


## `lxml`库

>`lxml`是一个`html/xml`的解析器，主要的功能是如何解析和提取`html`和`xml`数据

>`lxml`和正则一样是`c语言`实现的，是一款高性能的`python html/xml `解析器，我们可以利用之前学习的xpath语法来快速定位特定元素和节点信息

### 安装：

   * `pip install lxml` （网速还好可以用）

   * `pip install lxml -i https://pypi.douban.com/simple`（网速不好可以用）

### 使用`lxml`库来解析HTML代码：

   * 解析`html`字符串：使用`lxml.etree.HTML()`进行解析，示例代码如下：
```python
from lxml import etree
text = """
字符串类型的内容
"""
htmlElement = etree.HTML(text)
print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))

```

   * 解析文件（html），使用`lxml.etree.parse`来进行解析，示例代码如下：
```python
from lxml import etree
htmlElement = etree.parse("data.html")
print(etree.tostring(htmlElement,encoding= "utf-8").decode("utf-8"))
```

   * 这个函数默认使用`XML`解析器来解析，如果遇到不规范的`HTML`代码的时候就会解析报错，这个时候就要自己创建`HTML`解析器。
```python
from lxml import etree
parser = etree.HTMLParser(encoding="utf-8")
htmlElement = etree.parse("data.html",parser=parser)
print(etree.tostring(htmlElement,encoding="utf-8").decode("utf-8"))
```
