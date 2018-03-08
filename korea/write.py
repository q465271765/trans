from korea.Baidu_Translation import Baidu_Translation
from urllib import request
import json
import sys,urllib

"""
提取文件特征，调用googel翻译api，替换相应字符串
"""
# def django_trans(line):
#     if str(line).startswith('msgid'):
#         replace_str = line[str(line).find('"'):-1].replace('"', '')
#         from korea.google_translate import google_translate
#         result = google_translate(replace_str, 'en', 'ko')
#     return result
def google_translate(input,target_language,trans_language):
    input = urllib.parse.quote(input)
    res = request.urlopen("http://www.tastemylife.com/gtr.php?sl=" + target_language + "&tl=" + trans_language + "&p=2&q=" + input)
    html = res.read().decode('utf-8')
    result = json.loads(html)['result']
    return result


with open("django3.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
# 写的方式打开文件
is_replace = False
is_trans = False
with open("django1.txt", "w", encoding="utf-8") as f_w:
    for line in lines:
        if str(line).startswith('msgid') or is_trans == True:
            replace_str = line[str(line).find('"'):-1].replace('"', '')
            if len(replace_str) < 1:
                f_w.write(line)
                is_trans = True
                continue
            print(replace_str)
            trans_result = google_translate(str(replace_str), 'auto', 'ko')
            #trans_result = Baidu_Translation.TransInput(replace_str, 'en', 'zh')
            print(trans_result)
            is_replace = True
            is_trans = False
        if str(line).startswith('msgstr') and is_replace == True:
            try:
                replace_str = line[str(line).find('"'):-1].replace('"', '')
                if len(replace_str) == 0:
                    replace_str = '""'
                    trans_result = '"'+trans_result+'"'
                # if len(replace_str) == 0:
                #     f_w.write(line)
                #     continue
                print(replace_str)
                line = line.replace(replace_str, trans_result)
                is_replace = False
            except Exception as e:
                print(e)
                f_w.write(line)
                continue

        f_w.write(line)
