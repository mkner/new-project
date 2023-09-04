#! /usr/bin/env python

from setuptools import Command, Extension, setup
from setuptools.command.build_ext import build_ext


DISTNAME = "new-pkgsetup"
DESCRIPTION = "test project using setuptools"

if __name__ == "__main__":
    setup()
 
#mk  works 9/3

import as  newpkg

#import newpkg as somethingelse

