#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import os
import sys
from utils import ProjectProperties
from libraries import ToolFactory
tools = []


class Tools(object):

    def __init__(self, libraries):
        self.tools = []
        for lib in libraries:
            t = ToolFactory.generate_tool(lib)
            if t is not None:
                self.tools.append(t)


def detect_tools(ctx):
    tools = []
    if os.environ['PROJECT_ROOT']:
        libraries = ProjectProperties(os.environ['PROJECT_ROOT']).libraries
        tools = Tools(libraries).tools
    else:
        ctx.fatal('PROJECT_ROOT not defined, could not detect libraries')
    return tools


def options(opt):
    global tools
    tools = detect_tools(opt)
    opt.load(tools)


def configure(conf):
    global tools
    tools = detect_tools(conf)
    conf.load(tools)
