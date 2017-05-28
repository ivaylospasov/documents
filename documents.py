#!/usr/bin/env python3

from sys import argv
import subprocess
import glob

def list_doc_files():
    list_of_all_docs = glob.glob('*.doc*')
    return list_of_all_docs

def remove_additional_spaces():
    text = ' The       quick brown    fox'
    correct_text = " ".join(text.split())
    return correct_text

def main(filename):
    subprocess.run(['soffice', '--convert-to', 'txt', filename])


if __name__ == '__main__':
    main(argv[1])
