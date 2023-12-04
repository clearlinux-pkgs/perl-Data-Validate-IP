#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Data-Validate-IP
Version  : 0.31
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-IP-0.31.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-IP-0.31.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-validate-ip-perl/libdata-validate-ip-perl_0.27-1.debian.tar.xz
Summary  : 'IPv4 and IPv6 validation methods'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Validate-IP-license = %{version}-%{release}
Requires: perl-Data-Validate-IP-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(NetAddr::IP)
BuildRequires : perl(Test::Requires)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
Data::Validate::IP - IPv4 and IPv6 validation methods
# VERSION
version 0.31

%package dev
Summary: dev components for the perl-Data-Validate-IP package.
Group: Development
Provides: perl-Data-Validate-IP-devel = %{version}-%{release}
Requires: perl-Data-Validate-IP = %{version}-%{release}

%description dev
dev components for the perl-Data-Validate-IP package.


%package license
Summary: license components for the perl-Data-Validate-IP package.
Group: Default

%description license
license components for the perl-Data-Validate-IP package.


%package perl
Summary: perl components for the perl-Data-Validate-IP package.
Group: Default
Requires: perl-Data-Validate-IP = %{version}-%{release}

%description perl
perl components for the perl-Data-Validate-IP package.


%prep
%setup -q -n Data-Validate-IP-0.31
cd %{_builddir}
tar xf %{_sourcedir}/libdata-validate-ip-perl_0.27-1.debian.tar.xz
cd %{_builddir}/Data-Validate-IP-0.31
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Data-Validate-IP-0.31/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Validate-IP
cp %{_builddir}/Data-Validate-IP-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Data-Validate-IP/27d7d0cafe8116b4aaee8c0e933ad1cd2fac4d0e || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Data-Validate-IP/9f18915626be2c95f0505e40c51cae2f0cadb46e || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Validate::IP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Validate-IP/27d7d0cafe8116b4aaee8c0e933ad1cd2fac4d0e
/usr/share/package-licenses/perl-Data-Validate-IP/9f18915626be2c95f0505e40c51cae2f0cadb46e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
