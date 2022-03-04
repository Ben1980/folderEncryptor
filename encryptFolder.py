from ui import MainWindow
import wx

def main():
    app = wx.App(redirect=False)
    frame = MainWindow()
    app.MainLoop()

if __name__ == "__main__":
    main()
    