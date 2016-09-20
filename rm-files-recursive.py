#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

from common import recursive_file_search


def rmFile(rootDir, fileName, not_used_option):
    fullFilePath = os.path.join(rootDir, fileName)
    os.remove(fullFilePath)


def rmFiles(path, pattern):
    recursive_file_search.find_files_and_do(rmFile, path, pattern)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='Directory path for file looking')
    parser.add_argument('-p', default=None, help='Prefix of the file')
    args = parser.parse_args()
    rmFiles(args.d, args.p)
