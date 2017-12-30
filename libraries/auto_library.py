#! /usr/bin/env python
# encoding: utf-8
# Copyright Mac Clayton 2017

import utils


class AutoLibrary(object):

    def __init__(self, libs_vars, bin_vars=None):
        self._lib_vars = libs_vars
        self._bin_vars = bin_vars

    def libs_text(self):
        paths_text = '{}\n'.format(
            utils.convert_to_sys_comment(self.__class__.name()))
        for path in self._lib_vars:
            paths_text += '{}\n'.format(utils.convert_to_sys_env(path,
                                                                 self._lib_vars[path]))
        return paths_text

    def bin_text(self):
        env_var_format = ['%{}%'.format(var) for var in self._bin_vars]
        return ';'.join(env_var_format)

    @staticmethod
    def name():
        raise NotImplementedError("Subclasses should implement this!")

    @staticmethod
    def tool_name():
        raise NotImplementedError("Subclasses should implement this!")
