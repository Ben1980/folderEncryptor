from cProfile import label
from importlib.resources import path
from msilib.schema import Icon
from utils import encryptFolder
import wx
import pyperclip as pc
import os

class Encryptor(wx.Panel):
    path = ''
    password = ''

    def __init__(self, parent):
        super().__init__(parent)

        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.hBox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hBox1 = wx.BoxSizer(wx.HORIZONTAL)

        self.pwdLable = wx.StaticText(self, label='Generated Password')
        self.hBox2.Add(self.pwdLable, 0, wx.ALL, 5)

        self.pwd = wx.TextCtrl(self, value='')
        self.hBox2.Add(self.pwd, 0, wx.ALL, 5)

        self.btCopyToClipboard = wx.Button(self, label='Copy To Clipboard')
        self.btCopyToClipboard.Bind(wx.EVT_BUTTON, self.on_copy_to_clipboard)
        self.hBox2.Add(self.btCopyToClipboard, 0, wx.ALL, 5)

        self.selectFolder = wx.Button(self, label='Select Folder to Encrypt')
        self.selectFolder.Bind(wx.EVT_BUTTON, self.on_open)
        self.hBox1.Add(self.selectFolder, 0, wx.ALL, 5)

        self.encrypt = wx.Button(self, label='Encrypt')
        self.encrypt.Bind(wx.EVT_BUTTON, self.on_encrypt)
        self.encrypt.Disable()
        self.hBox1.Add(self.encrypt, 0, wx.ALL, 5)

        self.vBox.Add(self.hBox1, 0, wx.ALL, 5)
        self.vBox.Add(self.hBox2, 0, wx.ALL, 5)

        self.SetSizer(self.vBox)
        self.vBox.Fit(parent)
        self.Layout()

    def on_open(self, event):
        with wx.DirDialog(None, 'Choose a folder', '', wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.path = dialog.GetPath()
                self.encrypt.Enable(True)

    def on_encrypt(self, event):
        if self.path:
            self.password = encryptFolder(self.path)
            self.encrypt.Disable()
            self.pwd.Value = self.password
            with open(self.path + '/password_please_delete_this_file.log', 'w') as file:
                file.write(self.password)
            wx.MessageBox('Remember to delete ' + self.path, 'Alert', wx.ICON_EXCLAMATION | wx.STAY_ON_TOP)

    def on_copy_to_clipboard(self, event):
        if self.password:
            pc.copy(self.password)

class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Folder Encryptor', style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        panel = Encryptor(self)
        self.Show()
