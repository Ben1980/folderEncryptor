from cProfile import label
from msilib.schema import Icon
import wx

class Encryptor(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        vBox = wx.BoxSizer(wx.VERTICAL)
        hBox2 = wx.BoxSizer(wx.HORIZONTAL)
        hBox1 = wx.BoxSizer(wx.HORIZONTAL)

        pwdLable = wx.StaticText(self, label='Generated Password')
        hBox2.Add(pwdLable, 0, wx.ALL, 5)

        pwd = wx.TextCtrl(self, value='')
        hBox2.Add(pwd, 0, wx.ALL, 5)

        btCopyToClipboard = wx.Button(self, label='Copy To Clipboard')
        hBox2.Add(btCopyToClipboard, 0, wx.ALL, 5)

        selectFolder = wx.Button(self, label='Select Folder to Encrypt')
        hBox1.Add(selectFolder, 0, wx.ALL, 5)

        encrypt = wx.Button(self, label='Encrypt')
        hBox1.Add(encrypt, 0, wx.ALL, 5)

        vBox.Add(hBox1, 0, wx.ALL, 5)
        vBox.Add(hBox2, 0, wx.ALL, 5)

        self.SetSizer(vBox)
        vBox.Fit(parent)
        hBox1.Fit(parent)
        hBox2.Fit(parent)
        self.Layout()

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Engineering Ecryptor')
        panel = Encryptor(self)
        self.Show()
