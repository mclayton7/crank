#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

from libraries import *
from libraries.auto_library import AutoLibrary


def _get_lib_classnames():
    return AutoLibrary.__subclasses__()


class LibraryFactory(object):
    """Find the class that has a matching name via reflection"""
    @staticmethod
    def generate_library(lib_name):
        """Find the class that has a matching name via reflection"""
        for class_name in _get_lib_classnames():
            if class_name.name() in lib_name.keys():
                return class_name(lib_name[class_name.name()])
        else:
            lib_string = list(lib_name.keys())[0]
            raise NotImplementedError(
                '{} library not yet supported'.format(lib_string))


class ToolFactory(object):
    """Find the class that has a matching name via reflection"""
    @staticmethod
    def generate_tool(lib_name):
        """Find the class that has a matching name via reflection"""
        for class_name in _get_lib_classnames():
            if class_name.name() in lib_name.keys():
                return class_name.tool_name()
        else:
            lib_string = list(lib_name.keys())[0]
            raise NotImplementedError(
                '{} library not yet supported'.format(lib_string))
