%define upstream_name 	 Exporter-Lite
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Exporter-Lite perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Exporter/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality.  It supports "import()", @EXPORT and
@EXPORT_OK and not a whole lot else.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Exporter/Lite.pm
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 403163
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 268506
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2009.0
+ Revision: 210955
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.02-1mdv2008.0
+ Revision: 20078
- 0.02


* Fri Mar 31 2006 Buchan Milne <bgmilne@mandriva.org> 0.01-3mdk
- Rebuild
- use mkrel

* Fri Jun 17 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.01-2mdk
- Rebuild

* Thu Nov 27 2003 Stefan van der Eijk <stefan@eijk.nu> 0.01-1mdk
- initial mdk package

