%define modname uuid
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 78_%{modname}.ini

Summary:	UUID support functions for php
Name:		php-%{modname}
Version:	1.0.3
Release:	2
Group:		Development/PHP
License:	PHP License
URL:		https://pecl.php.net/package/%{modname}
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	ext2fs-devel
BuildRequires:	libuuid-devel
Provides:	php-pear-uuid
Obsoletes:	php-pear-uuid
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
[ "../package.xml" != "/" ] && rm -f ../package.xml

%files 
%defattr(-,root,root)
%doc CREDITS tests
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-1mdv2012.0
+ Revision: 806360
- 1.0.3

* Sun May 06 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-22
+ Revision: 796985
- fix build
- fix deps
- rebuild for php-5.4.x
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-20
+ Revision: 696486
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-19
+ Revision: 695487
- rebuilt for php-5.3.7

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-18
+ Revision: 646700
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-17mdv2011.0
+ Revision: 629897
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-16mdv2011.0
+ Revision: 628206
- ensure it's built without automake1.7

* Wed Nov 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-15mdv2011.0
+ Revision: 600546
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-14mdv2011.0
+ Revision: 588883
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-13mdv2010.1
+ Revision: 514711
- rebuilt for php-5.3.2

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-12mdv2010.1
+ Revision: 485498
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-11mdv2010.1
+ Revision: 468269
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-10mdv2010.0
+ Revision: 451640
- fix deps
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1.0.2-9mdv2010.0
+ Revision: 397302
- Rebuild

* Mon May 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-8mdv2010.0
+ Revision: 377040
- rebuilt for php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2009.1
+ Revision: 346683
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2009.1
+ Revision: 341846
- rebuilt against php-5.2.9RC2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2009.1
+ Revision: 323135
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-4mdv2009.1
+ Revision: 310318
- rebuilt against php-5.2.7

* Fri Jul 18 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-3mdv2009.0
+ Revision: 238466
- rebuild

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2009.0
+ Revision: 200282
- rebuilt for php-5.2.6

* Wed Apr 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2009.0
+ Revision: 192504
- 1.0.2

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-11mdv2008.1
+ Revision: 162259
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-10mdv2008.1
+ Revision: 107735
- restart apache if needed

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-9mdv2008.0
+ Revision: 77588
- rebuilt against php-5.2.4

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-8mdv2008.0
+ Revision: 39532
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-7mdv2008.0
+ Revision: 33885
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2008.0
+ Revision: 21365
- rebuilt against new upstream version (5.2.2)


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2007.0
+ Revision: 117638
- rebuilt against new upstream version (5.2.1)

* Thu Nov 09 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2007.0
+ Revision: 79298
- rebuild
- rebuilt for php-5.2.0
- Import php-uuid

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-2
- rebuilt for php-5.1.6

* Fri Aug 04 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
- renamed from php-pear-uuid to php-uuid

* Sun Jun 04 2006 David Walluck <walluck@mandriva.org> 0:1.0-1mdv2007.0
- 1.0
- release

