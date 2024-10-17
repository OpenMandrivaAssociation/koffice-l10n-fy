Name: koffice-l10n-fy
Version: 2.1.1
Release: %mkrel 1
Summary: Language files for KOffice Frisian
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/stable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-fy
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Frisian translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.1.1-1mdv2010.1
+ Revision: 491260
- new version 2.1.1

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2010.1
+ Revision: 469529
- new version 2.1.0

* Fri Nov 13 2009 Funda Wang <fwang@mandriva.org> 2.0.91-1mdv2010.1
+ Revision: 465548
- new version 2.0.91

* Thu Sep 17 2009 Funda Wang <fwang@mandriva.org> 2.0.82-1mdv2010.0
+ Revision: 443738
- new version 2.0.82

* Thu Aug 13 2009 Funda Wang <fwang@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 415819
- new version 2.0.2

* Sat Jun 27 2009 Funda Wang <fwang@mandriva.org> 2.0.1-1mdv2010.0
+ Revision: 389649
- new version 2.0.1

* Thu May 28 2009 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2010.0
+ Revision: 380403
- new versin 2.0.0
- new version 1.9.99.0

* Sun Feb 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.9.98.6-1mdv2009.1
+ Revision: 335948
- Update to beta6

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330486
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312697
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305041
- add source and spec
- Created package structure for koffice-l10n-fy.

