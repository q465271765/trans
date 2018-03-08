import sys,urllib
from urllib.request import urlopen
import json
import requests
import re
from urllib import request
#构造参数
#zipcode = sys.argv[1]
#wd = input("search word:")
#data = urllib.urlencode([('wd',wd)])

#构造url 不需要将参数拼接到url中
# url= "http://127.0.0.1:8000/trans"
# print ('ursing url', url)
#
# #构造request 只需要将参数放到urlopen的第二个参数里
# #req = urllib2.Request(url)
# fd = urlopen(url)
# result = fd.read()
# data = json.load(result)
# print(data)
# #读取相应结果
# while True:
#     for k in result:
#         print(k)
#,data={"input":"table","target_lang":"en","trans_lang":"kor" }
s = 'Delete out-of-date records, are you sure?'
s = urllib.parse.quote(s)
sl = 'en'
tl = 'zh-CN'
res = request.urlopen('https://ecs.aliyuncs.com/?Action=DescribeRegions')

print(res)
res = request.urlopen("http://www.tastemylife.com/gtr.php?sl="+sl+"&tl="+tl+"&p=2&q="+s)
#res = requests.get("http://127.0.0.1:8000/trans?input=table&target_lang=en&trans_lang=kor" )
html = res.read().decode('utf-8')
print(json.loads(html)['result'])
# 从返回页面中过滤出翻译后的文本

# 使用正则表达式匹配
# 翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
# .*? non-greedy or minimal fashion
# (?<=...)Matches if the current position in the string is preceded
# by a match for ... that ends at the current position
p = re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
m = p.search(html)
text_2 = m.group(0).strip(';')
print(text_2)
#print(res.text)