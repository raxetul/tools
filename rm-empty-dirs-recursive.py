#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

from common import recursive_file_search


def rmEmptyDir(dirPath):
    if not os.listdir(dirPath):
        os.rmdir(dirPath)


def rmEmptyDirs(path, pattern):
    recursive_file_search.find_dirs_and_do(rmEmptyDir, path, pattern)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='Directory path for looking')
    parser.add_argument('-p', default=None, help='Postfix of the file')
    args = parser.parse_args()
    rmEmptyDirs(args.d, args.p)
