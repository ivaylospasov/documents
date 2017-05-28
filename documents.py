#!/usr/bin/env python3

from os import path
from sys import argv
import subprocess
import glob


def get_filename(filename):
    file_name, file_extension = path.splitext(filename)
    txt_file = file_name + ".txt"
    return txt_file

def remove_additional_spaces():
    text = 'Подмяната			 на     батерии продължава '
    correct_text = " ".join(text.split())
    print(correct_text)
    return correct_text

def main(file_name):
    subprocess.run(['soffice', '--convert-to', 'txt', file_name])

def read_file(file):
    text_file = get_filename(file)
    with open(text_file, 'r') as f:
        read_data = f.read()
    return read_data


if __name__ == '__main__':
    main(argv[1])
    print(read_file(argv[1]))
