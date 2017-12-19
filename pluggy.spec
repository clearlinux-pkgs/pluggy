#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pluggy
Version  : 0.4.0
Release  : 24
URL      : https://pypi.debian.net/pluggy/pluggy-0.4.0.zip
Source0  : https://pypi.debian.net/pluggy/pluggy-0.4.0.zip
Summary  : plugin and hook calling mechanisms for python
Group    : Development/Tools
License  : MIT
Requires: pluggy-legacypython
Requires: pluggy-python3
Requires: pluggy-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Plugin registration and hook calling for Python
        ===============================================
        
        This is the plugin manager as used by pytest but stripped
        of pytest specific details.
        
        During the 0.x series this plugin does not have much documentation
        except extensive docstrings in the pluggy.py module.

%package legacypython
Summary: legacypython components for the pluggy package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pluggy package.


%package python
Summary: python components for the pluggy package.
Group: Default
Requires: pluggy-legacypython
Requires: pluggy-python3

%description python
python components for the pluggy package.


%package python3
Summary: python3 components for the pluggy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pluggy package.


%prep
%setup -q -n pluggy-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507164302
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test pluggy.py testing/test_pluggy.py
%install
export SOURCE_DATE_EPOCH=1507164302
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
