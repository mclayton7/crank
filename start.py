#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

from pathlib import Path
import yaml
import os
import sys
from libraries import *
from environment.environment import WindowsBuilder, LinuxBuilder
from utils import ProjectProperties


def generate_environment(name, libs):
    libraries = []
    for lib in libs:
        libraries.append(LibraryFactory.generate_library(lib))
    lib_text = ''
    bin_text = ''
    for library in libraries:
        lib_text += '\n{}'.format(library.libs_text())
        bin_text += '{};'.format(library.bin_text())
    if sys.platform == 'win32':
        return WindowsBuilder(lib_text, bin_text)
    else:
        return LinuxBuilder(lib_text, bin_text)


def write_start(environment):
    folder = Path(__file__).parents[1]
    file_path = os.path.join(folder, environment.filename())
    with open(file_path, 'w') as f:
        f.write(environment.text())


def main():
    folder = Path(__file__).parents[1]
    project = ProjectProperties(folder)
    start_file = generate_environment(project.name, project.libraries)
    write_start(start_file)

if __name__ == '__main__':
    main()
