#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/etc/profile.d")
    pisitools.dodir("/usr/share/java/maven/lib")
    pisitools.dodir("/usr/share/java/maven/boot")
    pisitools.dodir("/usr/share/java/maven/conf")
    pisitools.dodir("/usr/share/java/maven/bin")
    shelltools.export("JAVA_HOME","/usr/lib/jvm/java-7-openjdk")
    shelltools.system("sed '38i <property name=\"maven.home\" value=\"%s/usr/share/java/maven-%s\"\/>' build.xml > build2.xml" % (get.installDIR(), get.srcVERSION()))
    shelltools.export("M2_HOME","$maven.home")
    shelltools.export("PATH","$PATH:$M2_HOME/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/bin")
    shelltools.export("MAVEN_OPTS","-Xmx512m")
    shelltools.move("build2.xml","build.xml")
    shelltools.system("/usr/bin/ant -Dmaven.repo.local=%s/usr/share/java/maven/repo" % get.installDIR())
    pisitools.dosym("/usr/share/java/maven-3.0.5/bin/mvn","/usr/bin/mvn")
    pisitools.dosym("/usr/share/java/maven-3.0.5/bin/mvnDebug","/usr/bin/mvnDebug")
    pisitools.dosym("/usr/share/java/maven-3.0.5/bin/mvnyjp","/usr/bin/mvnyjp")
    pisitools.domove("/usr/share/java/maven/repo/","/usr/share/java/maven-%s/" % get.srcVERSION())
    pisitools.removeDir("/usr/share/java/maven")
