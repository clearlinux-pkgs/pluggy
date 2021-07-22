#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pluggy
Version  : 0.13.1
Release  : 71
URL      : https://files.pythonhosted.org/packages/f8/04/7a8542bed4b16a65c2714bf76cf5a0b026157da7f75e87cc88774aa10b14/pluggy-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/04/7a8542bed4b16a65c2714bf76cf5a0b026157da7f75e87cc88774aa10b14/pluggy-0.13.1.tar.gz
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
Provides: pypi(pluggy)

%description python3
python3 components for the pluggy package.


%prep
%setup -q -n pluggy-0.13.1
cd %{_builddir}/pluggy-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133611
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pluggy
cp %{_builddir}/pluggy-0.13.1/LICENSE %{buildroot}/usr/share/package-licenses/pluggy/67d360a32d3b3a723998ca8ac1fae5a242afbce7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pluggy/67d360a32d3b3a723998ca8ac1fae5a242afbce7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
