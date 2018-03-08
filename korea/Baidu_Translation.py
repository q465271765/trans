import hashlib
import json
import random
from urllib.request import urlopen
import urllib

class Baidu_Translation:
    def __init__(self):
        self._q = ''
        self._from = ''
        self._to = ''
        self._appid = 0
        self._key = ''
        self._salt = 0
        self._sign = ''
        self._dst = ''
        self._enable = True

    @classmethod
    def GetResult(self):
        #Trans = Baidu_Translation()
        # self._q.encode('utf8')
        m = str(self._appid) + self._q + str(self._salt) + self._key
        m_MD5 = hashlib.md5(m.encode(encoding='utf-8'))
        Baidu_Translation._sign = m_MD5.hexdigest()
        Url_1 = 'http://api.fanyi.baidu.' \
                'com/api/trans/vip/translate?'
        Url_2 = 'q=' + urllib.parse.quote(self._q) + '&from=' + self._from + '&to=' + self._to + '&appid=' + str(
            self._appid) + '&salt=' + str(self._salt) + '&sign=' + self._sign
        Url = Url_1 + Url_2
        #PostUrl = Url.decode()
        try:
            TransRequest = urlopen(Url)
            #TransResponse = urlopen(TransRequest)
            TransResult = TransRequest.read()
            data = json.loads(TransResult)
        except Exception as e:
            print(e)
            return
        if 'error_code' in data:
            print('Crash')
            print('error:', data['error_code'])
            return data['error_msg']
        else:
            self._dst = data['trans_result'][0]['dst']
            return self._dst

    def ShowResult(self, result):
        print
        result

    def Welcome(self):
        self._q = 'Welcome to use icedaisy online translation tool'
        self._from = 'auto'
        self._to = 'zh'
        self._appid = '20170720000065440'
        self._key = 'rPaUPX82FufZj2J966q7'
        self._salt = random.randint(10001, 99999)
        welcome = self.GetResult()
        print(welcome)
        self.ShowResult(welcome)

    @classmethod
    def TransInput(self,input,target_lang,trans_lang):
        self._q = input
        self._from = target_lang
        self._to = trans_lang
        self._appid = '20170720000065440'
        self._key = 'rPaUPX82FufZj2J966q7'
        self._salt = random.randint(10001, 99999)
        trans_info = self.GetResult()
        print(trans_info)
        return trans_info
        self.ShowResult(trans_info)


    def StartTrans(self):
        while self._enable:
            self._q = input()
            import operator
            if operator.eq(self._q, '!quit') == 0:
                self._enable = False
                print('Thanks for using!')
                break
            _q_len = len(self._q)
            if _q_len < 4096:
                result = self.GetResult()
                self.ShowResult(result)
            else:
                print('Exceeds the maximum limit of 4096 characters')


# Trans = Baidu_Translation()
# input ='白痴'
# target_lang = 'auto'
# trans_lang = 'kor'
# Trans.TransInput(input,target_lang,trans_lang)
# Trans.StartTrans()