#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pluggy
Version  : 0.8.0
Release  : 44
URL      : https://files.pythonhosted.org/packages/65/25/81d0de17cd00f8ca994a4e74e3c4baf7cd25072c0b831dad5c7d9d6138f8/pluggy-0.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/25/81d0de17cd00f8ca994a4e74e3c4baf7cd25072c0b831dad5c7d9d6138f8/pluggy-0.8.0.tar.gz
Summary  : plugin and hook calling mechanisms for python
Group    : Development/Tools
License  : MIT
Requires: pluggy-license = %{version}-%{release}
Requires: pluggy-python = %{version}-%{release}
Requires: pluggy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : python-core
BuildRequires : setuptools-legacypython
BuildRequires : setuptools_scm
BuildRequires : setuptools_scm-legacypython

%description
pluggy - A minimalist production ready plugin system
        ====================================================
        
        |pypi| |anaconda| |versions| |travis| |appveyor| |gitter| |black|
        
        This is the core framework used by the `pytest`_, `tox`_, and `devpi`_ projects.
        
        Please `read the docs`_ to learn more!
        
        A definitive example
        ====================

%package legacypython
Summary: legacypython components for the pluggy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pluggy package.


%package license
Summary: license components for the pluggy package.
Group: Default

%description license
license components for the pluggy package.


%package python
Summary: python components for the pluggy package.
Group: Default
Requires: pluggy-python3 = %{version}-%{release}

%description python
python components for the pluggy package.


%package python3
Summary: python3 components for the pluggy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pluggy package.


%prep
%setup -q -n pluggy-0.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539814429
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1539814429
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pluggy
cp LICENSE %{buildroot}/usr/share/package-licenses/pluggy/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pluggy/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
