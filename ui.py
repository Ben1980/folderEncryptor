import wx

class Encryptor(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Engineering Ecryptor')
        panel = Encryptor(self)
        self.Show()
