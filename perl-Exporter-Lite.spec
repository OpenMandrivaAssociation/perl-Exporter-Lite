%define module 	Exporter-Lite
%define version 0.02
%define release %mkrel 1

Summary:	Exporter-Lite perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Exporter/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 0:5.600
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildArch:	noarch

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality.  It supports "import()", @EXPORT and
@EXPORT_OK and not a whole lot else.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%doc README Changes
%{perl_vendorlib}/Exporter/Lite.pm
%{_mandir}/*/*


