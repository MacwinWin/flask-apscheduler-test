#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 06/26/21 10:55:53
# @File   : setup.py

import os
from distutils.core import setup
from Cython.Build import cythonize

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif os.path.splitext(fullPath)[-1] == '.py':
            allFiles.append(fullPath)

    return allFiles

listOfFiles = getListOfFiles('./swagger_server')

for file in listOfFiles:
    setup(ext_modules=cythonize(file, language_level = "3"))
    print(os.system(f'rm {os.path.splitext(file)[0]}.*'))
    print(os.system(f'mv *.so {os.path.split(file)[0]}'))
print(os.system('rm -r build'))