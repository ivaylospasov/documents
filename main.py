#!/usr/bin/env python3

from sys import argv
from os import path, getcwd, remove, listdir
import glob
import subprocess

# Convert document to txt file
# soffice --convert-to txt filename.doc

def list_doc_files():
    list_of_all_docs = glob.glob('*.doc*')
    return list_of_all_docs

def main():
    files = list_doc_files()
    for file in files:
        subprocess.run(['soffice', '--convert-to', 'txt', file])

if __name__ == '__main__':
    main()
