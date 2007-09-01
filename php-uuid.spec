%define modname uuid
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 78_%{modname}.ini

Summary:	UUID support functions for php
Name:		php-%{modname}
Version:	1.0
Release:	%mkrel 9
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/%{modname}
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tar.bz2
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	libext2fs-devel
Provides:	php-pear-uuid
Obsoletes:	php-pear-uuid
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This extension provides functions to generate and analyse universally unique
identifiers (UUIDs). It depends on the external libuuid. This library is
available on most linux  systems, its source is bundled with the ext2fs tools.

%prep

%setup -q -n %{modname}-%{version}

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}
%make

mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
[ "../package.xml" != "/" ] && rm -f ../package.xml

%files 
%defattr(-,root,root)
%doc CREDITS tests
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
