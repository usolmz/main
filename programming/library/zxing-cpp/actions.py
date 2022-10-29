#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-B build \
                            -DCMAKE_INSTALL_PREFIX=/usr \
                            -DCMAKE_BUILD_TYPE=None \
                            -DBUILD_EXAMPLES=OFF \
                            -DBUILD_BLACKBOX_TESTS=OFF")

def build():
    cmaketools.make("-C build")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("..")
    pisitools.dodoc("AUTHORS*", "LICENSE*", "README*")
