#!/usr/bin/env python3

from sys import argv
from os import path, getcwd, remove, listdir

# Convert document to txt file
# soffice --convert-to txt filename.doc

def list_files():
    current_dir = getcwd()
    yield listdir(current_dir)

'''
def convert_to_txt(files):
    for file in files:
        soffice --convert-to txt file
    pass
'''

def all_names():
    for file in list_files():
        print(file)


if __name__ == '__main__':
    #main()
    all_names()
