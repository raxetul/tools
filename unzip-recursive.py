#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import zipfile

from common import recursive_file_search


def unzipFile(rootDir, fileName, removeFile):
    fullFilePath = os.path.join(rootDir, fileName)
    zip_ref = zipfile.ZipFile(fullFilePath, 'r')
    zip_ref.extractall(rootDir)
    zip_ref.close()
    if removeFile:
        os.remove(fullFilePath)


def unzipFiles(path, pattern, removeFile):
    recursive_file_search.find_files_and_do(unzipFile, path, pattern, removeFile)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='Directory path for file looking')
    parser.add_argument('-p', default='*.zip', help='Postfix of the file, .zip should be at the end. ex: *foo*bar*.zip')
    parser.add_argument('-r', default=False, help='Remove after unzip, False|True')
    args = parser.parse_args()
    unzipFiles(args.d, args.p, args.r)
