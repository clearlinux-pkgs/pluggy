#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pluggy
Version  : 0.12.0
Release  : 53
URL      : https://files.pythonhosted.org/packages/75/21/cdabca0144cfa282c2893dc8e07957245ac8657896ef3ea26f18b6fda710/pluggy-0.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/75/21/cdabca0144cfa282c2893dc8e07957245ac8657896ef3ea26f18b6fda710/pluggy-0.12.0.tar.gz
Summary  : plugin and hook calling mechanisms for python
Group    : Development/Tools
License  : MIT
Requires: pluggy-license = %{version}-%{release}
Requires: pluggy-python = %{version}-%{release}
Requires: pluggy-python3 = %{version}-%{release}
Requires: importlib_metadata
BuildRequires : buildreq-distutils3
BuildRequires : importlib_metadata
BuildRequires : setuptools_scm

%description
pluggy - A minimalist production ready plugin system
        ====================================================
        
        |pypi| |conda-forge| |versions| |travis| |appveyor| |gitter| |black| |codecov|
        
        This is the core framework used by the `pytest`_, `tox`_, and `devpi`_ projects.
        
        Please `read the docs`_ to learn more!
        
        A definitive example
        ====================

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
%setup -q -n pluggy-0.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1560286690
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pluggy
cp LICENSE %{buildroot}/usr/share/package-licenses/pluggy/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pluggy/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
