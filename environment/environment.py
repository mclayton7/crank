#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import utils

class EnvironmentBuilder(object):
	def __init__(self, filename, text):
		self._filename = filename
		self._text = text

	def filename(self):
		return self._filename

	def text(self):
		return self._text


class WindowsBuilder(EnvironmentBuilder):
	def __init__(self, lib_text, bin_text):
		self._template = ''':: Copyright Mac Clayton 2017

@echo off
set PROJECT_ROOT=%~dp0

:: Libraries
{}
:: Waf
set WAF_EXECUTABLE=%PROJECT_ROOT%\\crank\\build\\waf

:: Path
set PATH={}%PATH%

:: Python Path
set PYTHONPATH=%PROJECT_ROOT%\\crank;%PROJECT_ROOT%\\crank\libraries;%PYTHONPATH%

:: Shortcuts
doskey waf=python %WAF_EXECUTABLE% $*
'''.format(lib_text, bin_text)
		super().__init__('start.bat', utils.convert_to_sys_paths(self._template))


class LinuxBuilder(EnvironmentBuilder):
	def __init__(self, lib_text, bin_text):
		self._template = '''#!/bin/sh
# Copyright Mac Clayton 2017

export PROJECT_ROOT=.

# Libraries
{}
# Waf
export WAF_EXECUTABLE=%PROJECT_ROOT%/crank/build/waf

# Path
export PATH={}%PATH%

# Shortcuts
doskey waf=python %WAF_EXECUTABLE% $*
'''.format(lib_text, bin_text)
		super().__init__('start.sh', utils.convert_to_sys_paths(self._template))
