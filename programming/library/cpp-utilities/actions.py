#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = ''.join([
    ' -DCMAKE_BUILD_TYPE=Release',
    ' -DBUILD_SHARED_LIBS=ON',
    ' -DUSE_STANDARD_FILESYSTEM=ON',
    ' -DFORCE_BOOST_IOSTREAMS_FOR_NATIVE_FILE_BUFFER=ON -L '
    ])

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(i, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../LICENSE", "../README.md")

