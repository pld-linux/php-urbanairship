%define		php_min_version  5.2.6
%define		pkgname	urbanairship
%include	/usr/lib/rpm/macros.php
Summary:	Urban Airship PHP library - web service API for iPhone push notifications
Name:		php-%{pkgname}
Version:	0.1
Release:	1
License:	?
Group:		Development/Languages/PHP
Source0:	https://github.com/urbanairship/php-library/tarball/master/%{pkgname}-%{version}.tgz
# Source0-md5:	4c0f3befc41103e40b86835262180492
URL:		https://github.com/urbanairship/php-library
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pear-HTTP_Request
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir			%{php_data_dir}/%{pkgname}

%description
This here is a PHP library for using the Urban Airship
<http://urbanairship.com/> web service API for iPhone push
notifications.

The library handles these parts of the API:
- device token registration
- basic push
- registering and pushing with tags
- broadcast
- feedback service
- device token deactivation (deregistration)
- device token listing

%prep
%setup -qc
mv urbanairship-php-library-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p urbanairship.php $RPM_BUILD_ROOT%{php_data_dir}
cp -p RESTClient.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p sample.php $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{php_data_dir}/urbanairship.php
%{php_data_dir}/RESTClient.php
%{_examplesdir}/%{name}-%{version}
