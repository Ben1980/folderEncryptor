import zipfile
import pyzipper
import os
import sys
import random
import string
import wx

def generatePassword():
    length = 45                      

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all,length)

    password = "".join(temp)
    return bytes(password, 'utf-8')

def encryptFolder(full_path):
    root_path = os.path.dirname(full_path)
    contents = os.walk(full_path)

    password = generatePassword()
    root_path = root_path.rstrip('\\')
    zip_name = full_path.replace(root_path + '\\', '')
    zip_name = root_path + '\\' + zip_name + '.zip'

    nb_files = 0;
    for root, folders, files in os.walk(full_path):
        nb_files += len(files)

    try:
        dialog = wx.ProgressDialog("File encryption in progress...", "Time remaining", nb_files, style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME)
        keepGoing = True

        with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_LZMA) as zf:
            zf.setpassword(password)
            zf.setencryption(pyzipper.WZ_AES, nbits=256)
            count = 0
            for root, folders, files in contents:
                for folder_name in folders:
                    absolute_path = os.path.join(root, folder_name)
                    relative_path = absolute_path.replace(root_path + '\\', '')
                    zf.write(absolute_path, relative_path)
                    if not keepGoing:
                        break
                for file_name in files:
                    absolute_path = os.path.join(root, file_name)
                    relative_path = absolute_path.replace(root_path + '\\','')
                    zf.write(absolute_path, relative_path)
                    count = count + 1
                    keepGoing  = dialog.Update(count)
                    if not keepGoing:
                        break

                if not keepGoing:
                        break

        dialog.Destroy()
    except IOError as message:
        print (message)
        sys.exit(1)
    except OSError as message:
        print(message)
        sys.exit(1)
    except zipfile.BadZipfile as message:
        print (message)
        sys.exit(1)
    finally:
        zf.close()
        return password.decode()
