from cProfile import label
import wx

class Encryptor(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        hBox = wx.BoxSizer(wx.HORIZONTAL)

        pwdLable = wx.StaticText(self, label='Generated Password')
        hBox.Add(pwdLable, 0, wx.ALL, 5)
        self.SetSizer(hBox)
        hBox.Fit(parent)
        self.Layout()

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Engineering Ecryptor')
        panel = Encryptor(self)
        self.Show()
