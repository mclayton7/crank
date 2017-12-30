#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import sys
import os


def convert_to_sys_env(var, path):
    if sys.platform == 'win32':
        return 'set {}={}'.format(var, path)
    else:
        return 'export {}={}'.format(var, path)


def convert_to_sys_comment(text):
    if sys.platform == 'win32':
        return ':: {}'.format(text)
    else:
        return '# {}'.format(text)


def convert_to_sys_paths(text):
    return text.replace('/', '\\')


def name_from_filename(filename):
    file_with_extension = os.path.split(filename)[1]
    file_without_extension = os.path.splitext(file_with_extension)[0]
    return file_without_extension
