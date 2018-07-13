%define upstream_name 	 Exporter-Lite
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Exporter-Lite perl module


License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Exporter/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Test::More)
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




