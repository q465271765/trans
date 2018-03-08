import wx
import requests
from urllib import request
import json
import urllib

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent,size=(690, 340),title=u'翻译小工具')


class ExamplePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.input = wx.TextCtrl(self, pos=(10, 50), size=(300, 200))
        self.output = wx.TextCtrl(self, pos=(330, 50), size=(300, 200))

        # the combobox Control
        self.sampleList = ['auto', 'zh', 'en', 'jp','ko']
        self.target_language = wx.ComboBox(self, pos=(20, 10), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN,value='auto')
        self.trans_language = wx.ComboBox(self, pos=(150, 10), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN,value='auto')

        self.button = wx.Button(self, label="翻译", pos=(250, 10),size=(95, -1))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button,self.target_language)

        self.quote = wx.StaticText(self, label="Autor:Jack.song", pos=(520, 270))

    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())

    def OnClick(self, event):
        self.output.Clear()
        target_language = self.target_language.Value
        trans_language = self.trans_language.Value
        if trans_language == 'auto':
            self.output.AppendText("请选择翻译语言")
            return
        input = self.input.Value
        if input == '':
            self.output.AppendText("请输入")
            return
        result = google_translate(input,target_language,trans_language)
        self.output.AppendText(result)
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())

    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()

    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())

def google_translate(input,target_language,trans_language):
    if target_language == 'zh':
        input = urllib.parse.quote(input)
    url_adress =  "http://www.tastemylife.com/gtr.php?"
    url_param =  "sl=" + target_language +"&tl=" + trans_language + "&p=1&q=" + input
    url = url_adress+url_param
    res = request.urlopen(url)
    html = res.read().decode('utf-8')
    result = json.loads(html)['result']
    return result

app = wx.App(False)
frame = MyFrame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()
