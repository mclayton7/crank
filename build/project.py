#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import sys


def windows(conf):
    conf.env.CXXFLAGS = [
        '/Z7',
        '/DEBUG',
        '/EHsc',
        '/DWINDOWS',
    ]


def linux(conf):
    pass


def configure(conf):
    if sys.platform == 'win32':
        windows(conf)
    else:
        linux(conf)
