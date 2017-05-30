#!/usr/bin/env python3

from os import path
from sys import argv
import subprocess
import glob


def get_filename(filename):
    file_name, file_extension = path.splitext(filename)
    txt_file = file_name + ".txt"
    return txt_file

def convert_to_txt(file_name):
    subprocess.run(['soffice', '--convert-to', 'txt', file_name])

def read_file(file):
    text_file = get_filename(file)
    with open(text_file, 'r') as f:
        read_data = f.readlines()
    return read_data

def remove_additional_spaces(text):
    text_for_correction = read_file(text)
    for line in text_for_correction:
        line = " ".join(line.split())
        print(line)


if __name__ == '__main__':
    convert_to_txt(argv[1])
    remove_additional_spaces(argv[1])
    #read_file(argv[1])
