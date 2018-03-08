from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
import random
from urllib.request import urlopen

# Create your views here.


def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


@csrf_exempt
def trans(response):

    # if response.method == "GET":
    #     language = {}
    #     language['auto'] = '自动检测'
    #     language['zh'] = '中文'
    #     language['en'] = '英语'
    #     language['jp'] = '日语'
    #     language['kor'] = '韩语'
    #     #return render(response, 'trans.html',{'language':language})
    #     return render(language)
    # if response.method == "POST":
    #     print('post')
        input = response.GET.get('input')
        target_lang = response.GET.get('target_lang')
        trans_lang = response.GET.get('trans_lang')
        from korea.Baidu_Translation import Baidu_Translation
        Trans = Baidu_Translation
        trans_info = Trans.TransInput(input,target_lang,trans_lang)
        return HttpResponse(trans_info)

        # @csrf_exempt
        # def trans(response):
        #
        #     if response.method == "GET":
        #         language = {}
        #         language['auto'] = '自动检测'
        #         language['zh'] = '中文'
        #         language['en'] = '英语'
        #         language['jp'] = '日语'
        #         language['kor'] = '韩语'
        #         # return render(response, 'trans.html',{'language':language})
        #         return render(language)
        #     if response.method == "POST":
        #         print('post')
        #         input = response.POST.get('input')
        #         target_lang = response.POST.get('target_lang')
        #         trans_lang = response.POST.get('trans_lang')
        #         from korea.Baidu_Translation import Baidu_Translation
        #         Trans = Baidu_Translation
        #         trans_info = Trans.TransInput(input, target_lang, trans_lang)
        #         return HttpResponse(trans_info)

# def GetResult(self):
#         self._q.encode('utf8')
#         m = str(self._appid) + self._q + str(self._salt) + self._key
#         m_MD5 = hashlib.md5(m)
#         self._sign = m_MD5.hexdigest()
#         Url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
#         Url_2 = 'q=' + self._q + '&from=' + self._from + '&to=' + self._to + '&appid=' + str(
#             self._appid) + '&salt=' + str(self._salt) + '&sign=' + self._sign
#         Url = Url_1 + Url_2
#         PostUrl = Url.decode()
#         TransRequest = urlopen.Request(PostUrl)
#         TransResponse = urlopen.urlopen(TransRequest)
#         TransResult = TransResponse.read()
#         data = json.loads(TransResult)
#         if 'error_code' in data:
#             print
#             'Crash'
#             print
#             'error:', data['error_code']
#             return data['error_msg']
#         else:
#             self._dst = data['trans_result'][0]['dst']
#             return self._dst
#
# def ShowResult(self, result):
#     print
#     result
#
#
#
# def TransInput(input,target_lang,trans_lang):
#     self._q = input
#     self._from = target_lang
#     self._to = trans_lang
#     self._appid = '20170720000065440'
#     self._key = 'rPaUPX82FufZj2J966q7'
#     self._salt = random.randint(10001, 99999)
#     trans_info = self.GetResult()
#     #print trans_info
#     self.ShowResult(trans_info)