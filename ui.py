import wx

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Engineering Ecryptor')
        panel = Encryptor(self, image_size=(240,240))
        self.Show()