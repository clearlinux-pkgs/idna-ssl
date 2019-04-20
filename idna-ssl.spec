#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : idna-ssl
Version  : 1.1.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/46/03/07c4894aae38b0de52b52586b24bf189bb83e4ddabfe2e2c8f2419eec6f4/idna-ssl-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/46/03/07c4894aae38b0de52b52586b24bf189bb83e4ddabfe2e2c8f2419eec6f4/idna-ssl-1.1.0.tar.gz
Summary  : Patch ssl.match_hostname for Unicode(idna) domains support
Group    : Development/Tools
License  : MIT
Requires: idna-ssl-python3
Requires: idna-ssl-license
Requires: idna-ssl-python
Requires: idna
BuildRequires : buildreq-distutils3
BuildRequires : idna
BuildRequires : pytest-runner

%description
========

%package license
Summary: license components for the idna-ssl package.
Group: Default

%description license
license components for the idna-ssl package.


%package python
Summary: python components for the idna-ssl package.
Group: Default
Requires: idna-ssl-python3

%description python
python components for the idna-ssl package.


%package python3
Summary: python3 components for the idna-ssl package.
Group: Default
Requires: python3-core

%description python3
python3 components for the idna-ssl package.


%prep
%setup -q -n idna-ssl-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534605543
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/idna-ssl
cp LICENSE %{buildroot}/usr/share/doc/idna-ssl/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/idna-ssl/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
