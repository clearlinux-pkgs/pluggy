#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pluggy
Version  : 0.13.1
Release  : 60
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
====================================================
pluggy - A minimalist production ready plugin system
====================================================

|pypi| |conda-forge| |versions| |travis| |appveyor| |gitter| |black| |codecov|

This is the core framework used by the `pytest`_, `tox`_, and `devpi`_ projects.

Please `read the docs`_ to learn more!

A definitive example
====================
.. code-block:: python

    import pluggy

    hookspec = pluggy.HookspecMarker("myproject")
    hookimpl = pluggy.HookimplMarker("myproject")


    class MySpec(object):
        """A hook specification namespace.
        """

        @hookspec
        def myhook(self, arg1, arg2):
            """My special little hook that you can customize.
            """


    class Plugin_1(object):
        """A hook implementation namespace.
        """

        @hookimpl
        def myhook(self, arg1, arg2):
            print("inside Plugin_1.myhook()")
            return arg1 + arg2


    class Plugin_2(object):
        """A 2nd hook implementation namespace.
        """

        @hookimpl
        def myhook(self, arg1, arg2):
            print("inside Plugin_2.myhook()")
            return arg1 - arg2


    # create a manager and add the spec
    pm = pluggy.PluginManager("myproject")
    pm.add_hookspecs(MySpec)

    # register plugins
    pm.register(Plugin_1())
    pm.register(Plugin_2())

    # call our ``myhook`` hook
    results = pm.hook.myhook(arg1=1, arg2=2)
    print(results)


Running this directly gets us::

    $ python docs/examples/toy-example.py
    inside Plugin_2.myhook()
    inside Plugin_1.myhook()
    [-1, 3]


.. badges

.. |pypi| image:: https://img.shields.io/pypi/v/pluggy.svg
    :target: https://pypi.org/pypi/pluggy

.. |versions| image:: https://img.shields.io/pypi/pyversions/pluggy.svg
    :target: https://pypi.org/pypi/pluggy

.. |travis| image:: https://img.shields.io/travis/pytest-dev/pluggy/master.svg
    :target: https://travis-ci.org/pytest-dev/pluggy

.. |appveyor| image:: https://img.shields.io/appveyor/ci/pytestbot/pluggy/master.svg
    :target: https://ci.appveyor.com/project/pytestbot/pluggy

.. |conda-forge| image:: https://img.shields.io/conda/vn/conda-forge/pluggy.svg
    :target: https://anaconda.org/conda-forge/pytest

.. |gitter| image:: https://badges.gitter.im/pytest-dev/pluggy.svg
    :alt: Join the chat at https://gitter.im/pytest-dev/pluggy
    :target: https://gitter.im/pytest-dev/pluggy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. |codecov| image:: https://codecov.io/gh/pytest-dev/pluggy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/pytest-dev/pluggy
    :alt: Code coverage Status

.. links
.. _pytest:
    http://pytest.org
.. _tox:
    https://tox.readthedocs.org
.. _devpi:
    http://doc.devpi.net
.. _read the docs:
   https://pluggy.readthedocs.io/en/latest/


=========
Changelog
=========

.. towncrier release notes start

pluggy 0.13.1 (2019-11-21)
==========================

Trivial/Internal Changes
------------------------

- `#236 <https://github.com/pytest-dev/pluggy/pull/236>`_: Improved documentation, especially with regard to references.


pluggy 0.13.0 (2019-09-10)
==========================

Trivial/Internal Changes
------------------------

- `#222 <https://github.com/pytest-dev/pluggy/issues/222>`_: Replace ``importlib_metadata`` backport with ``importlib.metadata`` from the
  standard library on Python 3.8+.


pluggy 0.12.0 (2019-05-27)
==========================

Features
--------

- `#215 <https://github.com/pytest-dev/pluggy/issues/215>`_: Switch from ``pkg_resources`` to ``importlib-metadata`` for entrypoint detection for improved performance and import time.  This time with ``.egg`` support.


pluggy 0.11.0 (2019-05-07)
==========================

Bug Fixes
---------

- `#205 <https://github.com/pytest-dev/pluggy/issues/205>`_: Revert changes made in 0.10.0 release breaking ``.egg`` installs.


pluggy 0.10.0 (2019-05-07)
==========================

Features
--------

- `#199 <https://github.com/pytest-dev/pluggy/issues/199>`_: Switch from ``pkg_resources`` to ``importlib-metadata`` for entrypoint detection for improved performance and import time.


pluggy 0.9.0 (2019-02-21)
=========================

Features
--------

- `#189 <https://github.com/pytest-dev/pluggy/issues/189>`_: ``PluginManager.load_setuptools_entrypoints`` now accepts a ``name`` parameter that when given will
  load only entry points with that name.

  ``PluginManager.load_setuptools_entrypoints`` also now returns the number of plugins loaded by the
  call, as opposed to the number of all plugins loaded by all calls to this method.



Bug Fixes
---------

- `#187 <https://github.com/pytest-dev/pluggy/issues/187>`_: Fix internal ``varnames`` function for PyPy3.


pluggy 0.8.1 (2018-11-09)
=========================

Trivial/Internal Changes
------------------------

- `#166 <https://github.com/pytest-dev/pluggy/issues/166>`_: Add ``stacklevel=2`` to implprefix warning so that the reported location of warning is the caller of PluginManager.


pluggy 0.8.0 (2018-10-15)
=========================

Features
--------

- `#177 <https://github.com/pytest-dev/pluggy/issues/177>`_: Add ``get_hookimpls()`` method to hook callers.



Trivial/Internal Changes
------------------------

- `#165 <https://github.com/pytest-dev/pluggy/issues/165>`_: Add changelog in long package description and documentation.


- `#172 <https://github.com/pytest-dev/pluggy/issues/172>`_: Add a test exemplifying the opt-in nature of spec defined args.


- `#57 <https://github.com/pytest-dev/pluggy/issues/57>`_: Encapsulate hook specifications in a type for easier introspection.


pluggy 0.7.1 (2018-07-28)
=========================

Deprecations and Removals
-------------------------

- `#116 <https://github.com/pytest-dev/pluggy/issues/116>`_: Deprecate the ``implprefix`` kwarg to ``PluginManager`` and instead
  expect users to start using explicit ``HookimplMarker`` everywhere.



Features
--------

- `#122 <https://github.com/pytest-dev/pluggy/issues/122>`_: Add ``.plugin`` member to ``PluginValidationError`` to access failing plugin during post-mortem.


- `#138 <https://github.com/pytest-dev/pluggy/issues/138>`_: Add per implementation warnings support for hookspecs allowing for both
  deprecation and future warnings of legacy and (future) experimental hooks
  respectively.



Bug Fixes
---------

- `#110 <https://github.com/pytest-dev/pluggy/issues/110>`_: Fix a bug where ``_HookCaller.call_historic()`` would call the ``proc``
  arg even when the default is ``None`` resulting in a ``TypeError``.

- `#160 <https://github.com/pytest-dev/pluggy/issues/160>`_: Fix problem when handling ``VersionConflict`` errors when loading setuptools plugins.



Improved Documentation
----------------------

- `#123 <https://github.com/pytest-dev/pluggy/issues/123>`_: Document how exceptions are handled and how the hook call loop
  terminates immediately on the first error which is then delivered
  to any surrounding wrappers.


- `#136 <https://github.com/pytest-dev/pluggy/issues/136>`_: Docs rework including a much better introduction and comprehensive example
  set for new users. A big thanks goes out to @obestwalter for the great work!



Trivial/Internal Changes
------------------------

- `#117 <https://github.com/pytest-dev/pluggy/issues/117>`_: Break up the main monolithic package modules into separate modules by concern


- `#131 <https://github.com/pytest-dev/pluggy/issues/131>`_: Automate ``setuptools`` wheels building and PyPi upload using TravisCI.


- `#153 <https://github.com/pytest-dev/pluggy/issues/153>`_: Reorganize tests more appropriately by modules relating to each
  internal component/feature. This is in an effort to avoid (future)
  duplication and better separation of concerns in the test set.


- `#156 <https://github.com/pytest-dev/pluggy/issues/156>`_: Add ``HookImpl.__repr__()`` for better debugging.


- `#66 <https://github.com/pytest-dev/pluggy/issues/66>`_: Start using ``towncrier`` and a custom ``tox`` environment to prepare releases!


pluggy 0.7.0 (Unreleased)
=========================

* `#160 <https://github.com/pytest-dev/pluggy/issues/160>`_: We discovered a deployment issue so this version was never released to PyPI, only the tag exists.

pluggy 0.6.0 (2017-11-24)
=========================

- Add CI testing for the features, release, and master
  branches of ``pytest`` (PR `#79`_).
- Document public API for ``_Result`` objects passed to wrappers
  (PR `#85`_).
- Document and test hook LIFO ordering (PR `#85`_).
- Turn warnings into errors in test suite (PR `#89`_).
- Deprecate ``_Result.result`` (PR `#88`_).
- Convert ``_Multicall`` to a simple function distinguishing it from
  the legacy version (PR `#90`_).
- Resolve E741 errors (PR `#96`_).
- Test and bug fix for unmarked hook collection (PRs `#97`_ and
  `#102`_).
- Drop support for EOL Python 2.6 and 3.3 (PR `#103`_).
- Fix ``inspect`` based arg introspection on py3.6 (PR `#94`_).

.. _#79: https://github.com/pytest-dev/pluggy/pull/79
.. _#85: https://github.com/pytest-dev/pluggy/pull/85
.. _#88: https://github.com/pytest-dev/pluggy/pull/88
.. _#89: https://github.com/pytest-dev/pluggy/pull/89
.. _#90: https://github.com/pytest-dev/pluggy/pull/90
.. _#94: https://github.com/pytest-dev/pluggy/pull/94
.. _#96: https://github.com/pytest-dev/pluggy/pull/96
.. _#97: https://github.com/pytest-dev/pluggy/pull/97
.. _#102: https://github.com/pytest-dev/pluggy/pull/102
.. _#103: https://github.com/pytest-dev/pluggy/pull/103


pluggy 0.5.2 (2017-09-06)
=========================

- fix bug where ``firstresult`` wrappers were being sent an incorrectly configured
  ``_Result`` (a list was set instead of a single value). Add tests to check for
  this as well as ``_Result.force_result()`` behaviour. Thanks to `@tgoodlet`_
  for the PR `#72`_.

- fix incorrect ``getattr``  of ``DeprecationWarning`` from the ``warnings``
  module. Thanks to `@nicoddemus`_ for the PR `#77`_.

- hide ``pytest`` tracebacks in certain core routines. Thanks to
  `@nicoddemus`_ for the PR `#80`_.

.. _#72: https://github.com/pytest-dev/pluggy/pull/72
.. _#77: https://github.com/pytest-dev/pluggy/pull/77
.. _#80: https://github.com/pytest-dev/pluggy/pull/80


pluggy 0.5.1 (2017-08-29)
=========================

- fix a bug and add tests for case where ``firstresult`` hooks return
  ``None`` results. Thanks to `@RonnyPfannschmidt`_ and `@tgoodlet`_
  for the issue (`#68`_) and PR (`#69`_) respectively.

.. _#69: https://github.com/pytest-dev/pluggy/pull/69
.. _#68: https://github.com/pytest-dev/pluggy/issues/68


pluggy 0.5.0 (2017-08-28)
=========================

- fix bug where callbacks for historic hooks would not be called for
  already registered plugins.  Thanks `@vodik`_ for the PR
  and `@hpk42`_ for further fixes.

- fix `#17`_ by considering only actual functions for hooks
  this removes the ability to register arbitrary callable objects
  which at first glance is a reasonable simplification,
  thanks `@RonnyPfannschmidt`_ for report and pr.

- fix `#19`_: allow registering hookspecs from instances.  The PR from
  `@tgoodlet`_ also modernized the varnames implementation.

- resolve `#32`_: split up the test set into multiple modules.
  Thanks to `@RonnyPfannschmidt`_ for the PR and `@tgoodlet`_ for
  the initial request.

- resolve `#14`_: add full sphinx docs. Thanks to `@tgoodlet`_ for
  PR `#39`_.

- add hook call mismatch warnings. Thanks to `@tgoodlet`_ for the
  PR `#42`_.

- resolve `#44`_: move to new-style classes. Thanks to `@MichalTHEDUDE`_
  for PR `#46`_.

- add baseline benchmarking/speed tests using ``pytest-benchmark``
  in PR `#54`_.  Thanks to `@tgoodlet`_.

- update the README to showcase the API. Thanks to `@tgoodlet`_ for the
  issue and PR `#55`_.

- deprecate ``__multicall__`` and add a faster call loop implementation.
  Thanks to `@tgoodlet`_ for PR `#58`_.

- raise a comprehensible error when a ``hookimpl`` is called with positional
  args. Thanks to `@RonnyPfannschmidt`_ for the issue and `@tgoodlet`_ for
  PR `#60`_.

- fix the ``firstresult`` test making it more complete
  and remove a duplicate of that test. Thanks to `@tgoodlet`_
  for PR `#62`_.

.. _#62: https://github.com/pytest-dev/pluggy/pull/62
.. _#60: https://github.com/pytest-dev/pluggy/pull/60
.. _#58: https://github.com/pytest-dev/pluggy/pull/58
.. _#55: https://github.com/pytest-dev/pluggy/pull/55
.. _#54: https://github.com/pytest-dev/pluggy/pull/54
.. _#46: https://github.com/pytest-dev/pluggy/pull/46
.. _#44: https://github.com/pytest-dev/pluggy/issues/44
.. _#42: https://github.com/pytest-dev/pluggy/pull/42
.. _#39: https://github.com/pytest-dev/pluggy/pull/39
.. _#32: https://github.com/pytest-dev/pluggy/pull/32
.. _#19: https://github.com/pytest-dev/pluggy/issues/19
.. _#17: https://github.com/pytest-dev/pluggy/issues/17
.. _#14: https://github.com/pytest-dev/pluggy/issues/14


pluggy 0.4.0 (2016-09-25)
=========================

- add ``has_plugin(name)`` method to pluginmanager.  thanks `@nicoddemus`_.

- fix `#11`_: make plugin parsing more resilient against exceptions
  from ``__getattr__`` functions. Thanks `@nicoddemus`_.

- fix issue `#4`_: specific ``HookCallError`` exception for when a hook call
  provides not enough arguments.

- better error message when loading setuptools entrypoints fails
  due to a ``VersionConflict``.  Thanks `@blueyed`_.

.. _#11: https://github.com/pytest-dev/pluggy/issues/11
.. _#4: https://github.com/pytest-dev/pluggy/issues/4


pluggy 0.3.1 (2015-09-17)
=========================

- avoid using deprecated-in-python3.5 getargspec method. Thanks
  `@mdboom`_.


pluggy 0.3.0 (2015-05-07)
=========================

initial release

.. contributors
.. _@hpk42: https://github.com/hpk42
.. _@tgoodlet: https://github.com/goodboy
.. _@MichalTHEDUDE: https://github.com/MichalTHEDUDE
.. _@vodik: https://github.com/vodik
.. _@RonnyPfannschmidt: https://github.com/RonnyPfannschmidt
.. _@blueyed: https://github.com/blueyed
.. _@nicoddemus: https://github.com/nicoddemus
.. _@mdboom: https://github.com/mdboom

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
export SOURCE_DATE_EPOCH=1583202659
# -Werror is for werrorists
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
