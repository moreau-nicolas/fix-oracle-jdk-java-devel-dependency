Summary: Fix Oracle JDK dependency
Name: fix-oracle-jdk-java-devel-dependency
Version: 1.0
Release: 1
License: GPL+
Group: Development/Tools
URL: http://perdu.com
Source0: fix-oracle-jdk-java-devel-dependency.tar.bz2

BuildArch: noarch
Requires: jdk
Provides: java-devel

%description
Oracle JDK RPM does not provide the expected "java-devel" dependency. It provides "jdk"
instead. This has an unfortunate effect: installing ant, maven or any tool that requires
java-devel will try and install openjdk. This is not desirable.
This RPM tries to find a "clean" solution to this problem, by creating a dummy package that requires "jdk" and provides "java-devel".

%prep
rm -rf $RPM_BUILD_DIR
mkdir -p $RPM_BUILD_DIR
cd $RPM_BUILD_DIR
tar -xjf $RPM_SOURCE_DIR/fix-oracle-jdk-java-devel-dependency.tar.bz2

%build

%install
install -d -m 0755 %{buildroot}/%{_datadir}/fix-oracle-jdk-java-devel-dependency/
install -m 0644 README %{buildroot}/%{_datadir}/fix-oracle-jdk-java-devel-dependency

%files
%{_datadir}/fix-oracle-jdk-java-devel-dependency/README

%changelog
