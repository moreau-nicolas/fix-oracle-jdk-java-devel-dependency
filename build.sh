#!/bin/bash

cd $(dirname $0)
tar -cjf fix-oracle-jdk-java-devel-dependency.tar.bz2 README
mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS,tmp}
mv fix-oracle-jdk-java-devel-dependency.tar.bz2 ~/rpmbuild/SOURCES/
mv fix-oracle-jdk-java-devel-dependency.spec ~/rpmbuild/SPECS/

rpmbuild -ba ~/rpmbuild/SPECS/fix-oracle-jdk-java-devel-dependency.spec
