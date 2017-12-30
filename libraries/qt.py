#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

from libraries.auto_library import AutoLibrary


class QtLibrary(AutoLibrary):

    def __init__(self, root_dir):
        lib_vars = {
            'QT5_ROOT': root_dir,
            'QT5_BIN': '%QT5_ROOT%/bin',
            'QT5_INCLUDES': '%QT5_ROOT%/include',
            'QT5_LIBDIR': '%QT5_ROOT%/lib',
            'QT5_XCOMPILE': '1',
        }
        bin_vars = ['QT5_BIN', 'QT5_LIBDIR']
        super().__init__(lib_vars, bin_vars)

    @staticmethod
    def name():
        return 'qt5'

    @staticmethod
    def tool_name():
        return 'qt5'
