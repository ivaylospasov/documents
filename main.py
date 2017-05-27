#!/usr/bin/env python3

from sys import argv
from os import path, getcwd, remove, listdir
import glob

# Convert document to txt file
# soffice --convert-to txt filename.doc

def list_doc_files():
    list_of_all_docs = glob.glob('*.doc*')
    return list_of_all_docs

'''
def convert_to_txt(files):
    for file in files:
        soffice --convert-to txt file
    pass
'''

def get_names():
    print(list_doc_files())

if __name__ == '__main__':
    get_names()
