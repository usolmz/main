#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --enable-external-ell   \
                         --disable-systemd-service \
                         --localstatedir=/var \
                         --with-dbus-busdir=/etc/dbus-1/systemd \
                         --enable-ofono          \
                         --enable-wired          \
                         --enable-hwsim          \
                         --enable-tools")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README*")
