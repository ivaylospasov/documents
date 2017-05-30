#!/usr/bin/env python3

from os import path, remove
from sys import argv
import subprocess
import glob

def get_filename(filename):
    file_name, file_extension = path.splitext(filename)
    return file_name

txt_extension = 'txt'
txt_file = get_filename(argv[1]) + '.' + txt_extension

def convert_to_txt(file):
    subprocess.run(['soffice', '--convert-to', txt_extension, file])

def read_and_write_file(file):
    with open(file, 'r') as rf:
        txt_file_ready = get_filename(file) + '_ready.' + txt_extension
        print(txt_file_ready)
        with open(txt_file_ready, 'w') as wf:
            for line in rf:
                line = " ".join(line.split())
                wf.write(line + '\n')
        try:
            remove(file)
        except OSError:
            pass


if __name__ == '__main__':
    get_filename(argv[1])
    convert_to_txt(argv[1])
    read_and_write_file(txt_file)
