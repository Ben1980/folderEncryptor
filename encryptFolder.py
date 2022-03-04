from tkinter import Tk, filedialog
from utils import encryptFolder


def main():
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

    dir_to_encrypt = filedialog.askdirectory() # Returns opened path as str

    password = encryptFolder(dir_to_encrypt)
    print('Password of Encrypted ' + dir_to_encrypt + ': ' + password)

if __name__ == "__main__":
    main()