# xpath语法和lxml模块

> xpath(XML PATH LANGUAGE)是一门在xml和html中查找信息的语言，可以用来在xml和html文档中对元素和属性进行遍历

## xpath开发工具

1、chrome插件： xpath helper

2、Firefox插件： xpath checker

## xpath语法
[详细语法](https://www.runoob.com/xpath/xpath-syntax.html)

`常用方法`

使用//获取整个页面中的元素，然后写标签名，然后再写谓语进行提取，比如：
```xpath
//div[@class = "abc"]
```

`需要注意的知识点`

1./和//的区别：/代表只获取直接子节点，//代表获取子孙节点，一般//用的比较多，当然也要视情况而定
2.contains：有时候某个属性中包含了多个值，那么可以使用`contains`函数，示例代码如下：
```xpath
//div[contains(@class,"jb_detail")]

```
3.谓语中的下表是从1开始的，不是从0开始的


## lxml库

lxml是一个html/xml的解析器，主要的功能是如何解析和提取html和xml数据

lxml和正则一样是c语言实现的，是一款高性能的python html/xml 解析器，我们可以利用之前学习的xpath语法来快速定位特定元素和节点信息

安装：
pip install lxml （网速还好可以用）
pip install lxml -i https://pypi.douban.com/simple（网速不好可以用）

### 基本使用

