import fnmatch
import os


def find_dirs_and_do(do_function, directory, pattern=None):
    for root, dirs, files in os.walk(directory):
        for basename in dirs:
            dirname = os.path.join(root, basename)
            # recursive call for sub directories
            find_dirs_and_do(do_function, dirname, pattern)
            if pattern == None or fnmatch.fnmatch(dirname, pattern):
                do_function(dirname)


def find_files_and_do(do_function, directory, pattern=None, option=False):
    for root, dirs, files in os.walk(directory):
        for basename in dirs:
            dirname = os.path.join(root, basename)
            # recursive call for sub directories
            find_files_and_do(do_function, dirname, pattern, option)
        for basename in files:
            if pattern == None or fnmatch.fnmatch(basename, pattern):
                print("Directory: ", root, "File: ", basename)
                do_function(root, basename, option)
