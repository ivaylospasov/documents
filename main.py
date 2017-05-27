#!/usr/bin/env python3

# Convert document to txt file
# soffice --convert-to txt filename.doc

def convert_to_txt(files):
    for file in files:
        soffice --convert-to txt file
