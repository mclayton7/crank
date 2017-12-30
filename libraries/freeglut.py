#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import os
from libraries.auto_library import AutoLibrary
from utils import name_from_filename


class FreeGlutLibrary(AutoLibrary):

    def __init__(self, root_dir):
        lib_vars = {
            'FREEGLUT_ROOT': root_dir,
            'FREEGLUT_INCLUDES': '%FREEGLUT_ROOT%/include',
            'FREEGLUT_LIBDIR': '%FREEGLUT_ROOT%/lib/x64',
            'FREEGLUT_BIN': '%FREEGLUT_ROOT%/bin/x64',
        }
        bin_vars = ['FREEGLUT_BIN']
        super().__init__(lib_vars, bin_vars)

    @staticmethod
    def name():
        return 'FreeGLUT'

    @staticmethod
    def tool_name():
        return name_from_filename(__file__)


def configure(conf):
    try:
        root_node = conf.root.find_node(os.environ['FREEGLUT_ROOT'])
        _includes = root_node.find_node('include').abspath()
        _libpath = [root_node.find_node('lib').find_node('x64').abspath()]

        conf.check_cxx(lib='freeglut', libpath=_libpath,
                       includes=_includes, uselib_store='GLUT')
        conf.check_cxx(lib='opengl32')

    except KeyError:
        conf.fatal('FREEGLUT_ROOT environment variable not defined')
