from urllib import request

response = request.urlopen("https://www.baidu.com")
request.urlretrieve("https://www.baidu.com","baidu.html")

# print(response)
# print(response.read())
# print(response.readline())
# print(response.readlines())
# print(response.getcode())