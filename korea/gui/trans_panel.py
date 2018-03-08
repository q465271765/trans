import wx
import requests
from urllib import request
import json
import urllib

class ExamplePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent,size = (600, 300))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.input = wx.TextCtrl(self, pos=(10, 50), size=(300, 200))
        self.output = wx.TextCtrl(self, pos=(330, 50), size=(300, 200))

        # the combobox Control
        self.sampleList = ['auto', 'zh', 'en', 'jp','kor']
        self.target_language = wx.ComboBox(self, pos=(20, 10), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN,value='auto')
        self.trans_language = wx.ComboBox(self, pos=(150, 10), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN,value='auto')

        self.button = wx.Button(self, label="翻译", pos=(250, 10),size=(95, -1))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button,self.target_language)


    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())

    def OnClick(self, event):
        self.output.Clear()
        target_language = self.target_language.Value
        trans_language = self.trans_language.Value
        input = self.input.Value
        #后台
        # url = "http://127.0.0.1:8000/trans?input="+input+"&target_lang="+target_language+"&trans_lang="+trans_language
        # res = requests.get(url)
        # self.output.AppendText(res.text)
        #google translate
        if trans_language=='zh':
            input = urllib.parse.quote(input)
        res = request.urlopen("http://www.tastemylife.com/gtr.php?sl="+target_language+
                              "&tl="+trans_language+"&p=1&q="+input)
        # res = requests.get("http://127.0.0.1:8000/trans?input=table&target_lang=en&trans_lang=kor" )
        html = res.read().decode('utf-8')
        result = json.loads(html)['result']
        self.output.AppendText(result)
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())

    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()

    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())


app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
