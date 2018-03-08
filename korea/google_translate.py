# -*- coding: utf-8 -*-
# Python -V: Python 2.6.6
# filename:GoogleTranslation1.2.py

__author__ = "Yinlong Zhao (zhaoyl[at]sjtu[dot]edu[dot]cn)"
__date__ = "$Date: 2013/04/21 $"

import re
import urllib
from urllib.request import urlopen
from urllib import request
import json

# urllib:
# urllib2: The urllib2 module defines functions and classes which help in opening
# URLs (mostly HTTP) in a complex world — basic and digest authentication,
# redirections, cookies and more.



def translate(text):
    '''''模拟浏览器的行为，向Google Translate的主页发送数据，然后抓取翻译结果 '''

    # text 输入要翻译的英文句子
    text_1 = text
    # 'langpair':'en'|'zh-CN'从英语到简体中文
    values = {'hl': 'zh-CN', 'ie': 'UTF-8', 'text': text_1, 'langpair': "'en'|'zh-CN'"}
    url = 'http://translate.google.cn/translate_t'
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url, data)
    # 模拟一个浏览器
    browser = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
    req.add_header('User-Agent', browser)
    # 向谷歌翻译发送请求
    response = urllib.request.urlopen(req)
    # 读取返回页面
    html = response.read()
    # 从返回页面中过滤出翻译后的文本
    # 使用正则表达式匹配
    # 翻译后的文本是'TRANSLATED_TEXT='等号后面的内容
    # .*? non-greedy or minimal fashion
    # (?<=...)Matches if the current position in the string is preceded
    # by a match for ... that ends at the current position
    p = re.compile(r"(?<=TRANSLATED_TEXT=).*?;")
    m = p.search(html)
    text_2 = m.group(0).strip(';')
    return text_2

def google_translate(input,target_language,trans_language):

    input = urllib.parse.quote(input)
    # url_adress =  "http://www.tastemylife.com/gtr.php?"
    # url_param =  "sl=" + target_language +"&tl=" + trans_language + "&p=1&q="+input
    # url = url_adress+url_param
    # print(url)
    #res = request.urlopen("http://www.tastemylife.com/gtr.php?sl="+target_language+"&tl="+trans_language+"&p=2&q=Delete out-of-date records, are you sure?")
    res = request.urlopen("http://www.tastemylife.com/gtr.php?sl=" + target_language + "&tl=" + trans_language + "&p=2&q=" + input)
    html = res.read().decode('utf-8')
    result = json.loads(html)['result']
    return result



if __name__ == "__main__":
    # text_1 原文
    # text_1=open('c:\\text.txt','r').read()
    text_1 = 'Hello, my name is Derek. Nice to meet you! '
    print('The input text: %s' % text_1)
    text_2 = translate(text_1).strip("'")
    print('The output text: %s' % text_2)

    # 保存结果
    filename = 'c:\\Translation.txt'
    fp = open(filename, 'w')
    fp.write(text_2)
    fp.close()

    report = 'Master, I have done the work and saved the translation at ' + filename + '.'
    print('Report: %s' % report)