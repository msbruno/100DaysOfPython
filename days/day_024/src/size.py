'''
Print all file with respective size in MB.
'''

import os
import math

MEGA_BYTE = math.pow(1024, 2)
PATH = 'absolute-path'

def to_mega(byte_size):
   return byte_size / MEGA_BYTE

def file_size(path:str):
   return os.stat(path).st_size

for dirpath, dirnames, filenames in os.walk(PATH):
    for filename in filenames:
        path = (os.path.join(dirpath, filename))
        size_byte = file_size(path)
        size_mb = to_mega(size_byte)
        print("{} size is -> {} MB".format(path, size_mb))
