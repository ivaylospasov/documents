#!/usr/bin/env python3

from os import path, remove, linesep
from sys import argv
import subprocess
import json


def get_filename(filename):
    file_name, file_extension = path.splitext(filename)
    return file_name

scripts_path = path.dirname(argv[0])
corrections_json = scripts_path + '/' + 'corrections.json'
txt_ext = 'txt'
txt_file = get_filename(argv[1]) + '.' + txt_ext
txt_file_ready = get_filename(argv[1]) + '_ready' + '.' + txt_ext

def corrections_data():
    with open(corrections_json) as data_file:
        data = json.load(data_file)
        return data

def convert_to_txt(file):
    subprocess.run(['soffice', '--convert-to', 'txt', file])

def remove_additional_spaces(file):
    with open(file, 'r') as rf:
        with open(txt_file_ready, 'w') as wf:
            for line in rf:
                if line.strip():
                    line = " ".join(line.split())
                    wf.write(line + '\n\n')
        try:
            remove(file)
        except OSError:
            pass

def loop_corrections(file, dict):
    with open(file, 'r') as rf:
        with open('corrected_signs.txt', 'w') as wf:
            for line in rf:
                if line.strip():
                    for key, wrong_words in dict.items():
                        for wrong_word in wrong_words:
                            line = line.replace(wrong_word, key)
                    wf.write(line)


if __name__ == '__main__':
    convert_to_txt(argv[1])
    remove_additional_spaces(txt_file)
    loop_corrections(txt_file_ready, corrections_data())
    remove_additional_spaces('corrected_signs.txt')
