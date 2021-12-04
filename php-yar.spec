#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-yar
Version  : 2.2.0
Release  : 16
URL      : https://pecl.php.net/get/yar-2.2.0.tgz
Source0  : https://pecl.php.net/get/yar-2.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-yar-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : curl-dev

%description
No detailed description available

%package lib
Summary: lib components for the php-yar package.
Group: Libraries

%description lib
lib components for the php-yar package.


%prep
%setup -q -n yar-2.2.0
cd %{_builddir}/yar-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/yar.so
