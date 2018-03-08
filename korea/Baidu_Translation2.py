import urllib2
import hashlib
import json
import random


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

    def GetResult(self):
        self._q.encode('utf8')
        m = str(Trans._appid) + Trans._q + str(Trans._salt) + Trans._key
        m_MD5 = hashlib.md5(m)
        Trans._sign = m_MD5.hexdigest()
        Url_1 = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
        Url_2 = 'q=' + self._q + '&from=' + self._from + '&to=' + self._to + '&appid=' + str(
            Trans._appid) + '&salt=' + str(Trans._salt) + '&sign=' + self._sign
        Url = Url_1 + Url_2
        PostUrl = Url.decode()
        TransRequest = urllib2.Request(PostUrl)
        TransResponse = urllib2.urlopen(TransRequest)
        TransResult = TransResponse.read()
        data = json.loads(TransResult)
        if 'error_code' in data:
            print
            'Crash'
            print
            'error:', data['error_code']
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
        self.ShowResult(welcome)

    def StartTrans(self):
        while self._enable:
            self._q = raw_input()
            if cmp(self._q, '!quit') == 0:
                self._enable = False
                print
                'Thanks for using!'
                break
            _q_len = len(self._q)
            if _q_len < 4096:
                result = self.GetResult()
                self.ShowResult(result)
            else:
                print
                'Exceeds the maximum limit of 4096 characters'



Trans = Baidu_Translation()
Trans.Welcome()
Trans.StartTrans()
