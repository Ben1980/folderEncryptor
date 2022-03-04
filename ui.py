from cProfile import label
from msilib.schema import Icon
import wx

class Encryptor(wx.Panel):
    path = ''

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
        selectFolder.Bind(wx.EVT_BUTTON, self.on_open)
        hBox1.Add(selectFolder, 0, wx.ALL, 5)

        encrypt = wx.Button(self, label='Encrypt')
        hBox1.Add(encrypt, 0, wx.ALL, 5)

        vBox.Add(hBox1, 0, wx.ALL, 5)
        vBox.Add(hBox2, 0, wx.ALL, 5)

        self.SetSizer(vBox)
        vBox.Fit(parent)
        self.Layout()

    def on_open(self, event):
        with wx.DirDialog(None, 'Choose a folder', '', wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.path.SetValue(dialog.GetPath())

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Engineering Ecryptor')
        panel = Encryptor(self)
        self.Show()
