import zipfile
import pyzipper
import os
import sys
import random
import string

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

    try:
        with pyzipper.AESZipFile(zip_name, 'w', compression=pyzipper.ZIP_LZMA) as zf:
            zf.setpassword(password)
            zf.setencryption(pyzipper.WZ_AES, nbits=256)
            for root, folders, files in contents:
                for folder_name in folders:
                    absolute_path = os.path.join(root, folder_name)
                    relative_path = absolute_path.replace(root_path + '\\', '')
                    zf.write(absolute_path, relative_path)
                for file_name in files:
                    absolute_path = os.path.join(root, file_name)
                    relative_path = absolute_path.replace(root_path + '\\','')
                    zf.write(absolute_path, relative_path)

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
