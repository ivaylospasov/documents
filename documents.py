#!/usr/bin/env python3

from os import path, remove
from sys import argv
import subprocess
import json
from pprint import pprint


signs_wrong = [' ,', ' .', ' :', ' ;', '“', '„', '”', ' й ', '¤', \
'по - ', 'по- ', 'по -', \
'най - ', 'най- ', 'най -', \
' бул. ', ' БУЛ. ', ' ул. ', ' УЛ. ', ' ЕС', ' пл. ', \
' хил.', ' млн.', ' лв.']
signs_right = [', ', '. ', ': ', '; ', '"', '"', '"', ' ѝ ', '', \
'по-', 'по-', 'по-', \
'най-', 'най-', 'най-', \
' булевард ', ' булевард ', ' улица ', ' улица ', ' Европейския съюз', ' площад ' \
' хиляди', ' милиона', ' лева']

corrections = {
", ": [" ,"],
". ": [" ."],
": ": [" :"],
"\"": ["“", "„", "”"],
" ѝ ": [" й "],
"по-": ["по - ", "по- ", "по -"],
"най-": ["най - ", "най- ", "най -"],
" площад ":[" пл. ", " ПЛ. "]
}

def get_filename(filename):
    file_name, file_extension = path.splitext(filename)
    return file_name

scripts_path = path.dirname(argv[0])
corrections_json = scripts_path + '/' + 'corrections.json'
txt_extension = 'txt'
txt_file = get_filename(argv[1]) + '.' + txt_extension
txt_file_ready = get_filename(argv[1]) + '_ready.' + txt_extension

with open(corrections_json) as data_file:
    data = json.load(data_file)

def convert_to_txt(file):
    subprocess.run(['soffice', '--convert-to', txt_extension, file])

def read_and_write_file(file):
    with open(file, 'r') as rf:
        with open(txt_file_ready, 'w') as wf:
            for line in rf:
                line = " ".join(line.split())
                wf.write(line + '\n')
        try:
            remove(file)
        except OSError:
            pass

def correct_space_and_sign(file):
    with open(file, 'r') as rf:
        with open('corrected_signs.txt', 'w') as wf:
            for line in rf:
                for wrong, right in zip(signs_wrong, signs_right):
                    line = line.replace(wrong, right)
                wf.write(line)

def loop_corrections(dict):
    for key, value in dict.items():
        for wrong_word in value:
            print(wrong_word + ' се замества с ' + key)

if __name__ == '__main__':
    get_filename(argv[1])
    convert_to_txt(argv[1])
    read_and_write_file(txt_file)
    correct_space_and_sign(txt_file_ready)
    read_and_write_file('corrected_signs.txt')
    loop_corrections(corrections)
