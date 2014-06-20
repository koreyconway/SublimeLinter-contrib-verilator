#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Korey,,,
# Copyright (c) 2014 Korey,,,
#
# License: MIT
#

"""This module exports the Verilator plugin class."""

from SublimeLinter.lint import Linter, util


class Verilator(Linter):

    """Provides an interface to verilator."""

    syntax = ('verilog', 'systemverilog')
    cmd = 'verilator --lint-only'
    regex = r'\%(?:(?P<error>Error.*?)|(?P<warning>Warning).*?):.+?:(?P<line>.+?): (?P<message>.+)'
    tempfile_suffix = '_temp'
