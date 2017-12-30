#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import yaml
import os


class ProjectProperties(object):

    def __init__(self, directory):
        yaml = self._read_yaml(directory)
        (self.name, self.libraries) = self._parse_yaml(yaml)

    def _parse_yaml(self, yaml):
        name = yaml['name']
        libraries = yaml['libraries']
        return (name, libraries)

    def _read_yaml(self, directory):
        file = os.path.join(directory, 'ProjectProperties.yaml')
        with open(file) as f:
            return yaml.safe_load(f)
