#!/usr/bin/env python3

from sys import argv
import subprocess
import glob


def remove_additional_spaces():
    text = 'Подмяната			 на     батерии продължава '
    correct_text = " ".join(text.split())
    print(correct_text)
    return correct_text

def main(script, *argv):
    for file in argv:
        subprocess.run(['soffice', '--convert-to', 'txt', file])


if __name__ == '__main__':
    main(*argv)
