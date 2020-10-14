# from urllib import parse
# date = {
#     "name": "张三" ,
#     "age" : 18,
#     "sex" : "male"
#     }
#
# qs = parse.urlencode(date)
# print(qs)
#
# result = parse.parse_qs(qs)
# print(result)
#

#
# from urllib import parse
#
# url = "https://www.baidu.com/s;hello word?wd=hello word&username=123#date"
#
# result1 = parse.urlparse(url)
# result2 = parse.urlsplit(url)
# print(result1)
# print(result2)
# print("scheme：",result1.scheme)
# print("netloc：",result1.netloc)
# print("path：",result1.path)
# print("params：",result1.params)
# print("query：",result1.query)
# print("fragment：",result1.fragment)
#
#
# print("scheme：",result2.scheme)
# print("netloc：",result2.netloc)
# print("path：",result2.path)
# print("query：",result2.query)
# print("fragment：",result2.fragment)
# name=%E5%BC%A0%E4%B8%89&age=18&sex=male
# {'name': ['张三'], 'age': ['18'], 'sex': ['male']}
# response = request.urlopen("https://www.baidu.com")
# request.urlretrieve("https://www.baidu.com","baidu.html")
# request.urlretrieve("https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1602244848418&di=55f89cc9014c7439c658df9539cdd59d&imgtype=0&src=http%3A%2F%2F01imgmini.eastday.com%2Fmobile%2F20200210%2F20200210124632_dce5fc05ecccb056da40c72aa8c0fe52_1.jpeg","urllib库/kai.png")
# print(response)
# print(response.read())
# print(response.readline())
# print(response.readlines())
# print(response.getcode())
#
# #
# import http.cookiejar
# from urllib import request,parse
# import time
#
# url = "https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false"
#
# form = {
#     "first": "true",
#     "pn": 1,
#     "kd": "Python"
# }
#
# headers = {
#     "origin": "https://www.lagou.com",
#     "referer": "https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=",
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
# }
#
# cookie = http.cookiejar.CookieJar()
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# # res = request.Request(url="https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=", headers=headers,data=parse.urlencode(form).encode("utf-8"),method="GET")
# # opener.open(url="https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=")
# resp = request.Request(url='https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=', headers=headers)
# response = opener.open(resp,data=parse.urlencode(form).encode("utf-8"))
#
# time.sleep(5)
#
# resp = request.Request(url, headers=headers)
# response1 = opener.open(resp,data=parse.urlencode(form).encode("utf-8"))
# # res = request.urlopen(resp,timeout=5)
#
# # result= request.urlopen(resp,timeout=5)
#
# print(response1.read().decode("utf-8"))
# import json
# import requests
# import xlwt
# import time
#
#
# # 获取存储职位信息的json对象，遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、发布时间、职位名称、薪资、工作年限
# def get_json(url, datas):
#     my_headers = {
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
#         "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
#         "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
#     }
#     time.sleep(5)
#     ses = requests.session()  # 获取session
#     ses.headers.update(my_headers)  # 更新
#     ses.get(
#         "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=")
#     content = ses.post(url=url, data=datas)
#     result = content.json()
#     info = result['content']['positionResult']['result']
#     info_list = []
#     for job in info:
#         information = []
#         information.append(job['positionId'])  # 岗位对应ID
#         information.append(job['city'])  # 岗位对应城市
#         information.append(job['companyFullName'])  # 公司全名
#         information.append(job['companyLabelList'])  # 福利待遇
#         information.append(job['district'])  # 工作地点
#         information.append(job['education'])  # 学历要求
#         information.append(job['firstType'])  # 工作类型
#         information.append(job['formatCreateTime'])  # 发布时间
#         information.append(job['positionName'])  # 职位名称
#         information.append(job['salary'])  # 薪资
#         information.append(job['workYear'])  # 工作年限
#         info_list.append(information)
#         # 将列表对象进行json格式的编码转换,其中indent参数设置缩进值为2
#         # print(json.dumps(info_list, ensure_ascii=False, indent=2))
#     # print(info_list)
#     return info_list
#
#
# def main():
#     page = int(input('请输入你要抓取的页码总数：'))
#     # kd = input('请输入你要抓取的职位关键字：')
#     # city = input('请输入你要抓取的城市：')
#
#     info_result = []
#     title = ['岗位id', '城市', '公司全名', '福利待遇', '工作地点', '学历要求', '工作类型', '发布时间', '职位名称', '薪资', '工作年限']
#     info_result.append(title)
#     for x in range(1, page + 1):
#         url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
#         datas = {
#             'first': 'false',
#             'pn': x,
#             'kd': 'python',
#         }
#         try:
#             info = get_json(url, datas)
#             info_result = info_result + info
#             print("第%s页正常采集" % x)
#         except Exception as msg:
#             print("第%s页出现问题" % x)
#
#         # 创建workbook,即excel
#         workbook = xlwt.Workbook(encoding='utf-8')
#         # 创建表,第二参数用于确认同一个cell单元是否可以重设值
#         worksheet = workbook.add_sheet('lagouzp', cell_overwrite_ok=True)
#         for i, row in enumerate(info_result):
#             # print(row)
#             for j, col in enumerate(row):
#                 # print(col)
#                 worksheet.write(i, j, col)
#         workbook.save('lagouzp.xls')
#
#
# if __name__ == '__main__':
#     main()


#
# import requests
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
# }
#
# params = {
#     "wd":"中国",
# }
#
# # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
# response = requests.get("http://www.baidu.com/s",params=params)
#
# # 查看响应的内容，response.text返回的是Unicode格式数据,会自动识别编码格式，但是会出现识别出错问题
# print(response.text)
#
# # with open("baidu.html","w",encoding="utf-8") as f:
# #     f.write(response.text)
#
# # 查看响应的内容，response.content返回的是字节流数据，可以自行进行的解码，指定解码格式
# print(response.content)
# # with open("baidu.html","w",encoding="utf-8") as f:
# #     f.write(response.content.decode("utf-8"))
#
# # 查看完整的url地址
# print(response.url)
#
# # 查看响应的头部信息的字符串编码格式
# print(response.encoding)
#
# # 查看响应码
# print(response.status_code)

import requests

url = "http://httpbin.org/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
}

proxy = {
    'http': '121.236.124.219:57114'
}

resp = requests.get(url,headers=headers,proxies=proxy)
with open('xx.html','w',encoding='utf-8') as fp:
    fp.write(resp.text)