#!/usr/bin/env python3

from sys import argv
from os import path, getcwd, remove, listdir
import glob
import subprocess
#import re

def list_doc_files():
    list_of_all_docs = glob.glob('*.doc*')
    return list_of_all_docs

def remove_additional_spaces():
    '''
    Use re just for spaces, but not for tabs
    correct_text = re.sub(' +', ' ', text)
    '''
    text = ' The       quick brown    fox'
    correct_text = " ".join(text.split())
    return correct_text

def main():
    file = argv[1]
    subprocess.run(['soffice', '--convert-to', 'txt', file])

def print_arguments():
    print(argv[1])

if __name__ == '__main__':
    #print(remove_additional_spaces())
    main()
