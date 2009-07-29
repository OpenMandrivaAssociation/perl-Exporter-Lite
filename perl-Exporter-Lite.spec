%define upstream_name 	 Exporter-Lite
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Exporter-Lite perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Exporter/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is an alternative to Exporter intended to provide a lightweight
subset of its functionality.  It supports "import()", @EXPORT and
@EXPORT_OK and not a whole lot else.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
