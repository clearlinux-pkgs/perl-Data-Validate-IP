#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Validate-IP
Version  : 0.27
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-IP-0.27.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-IP-0.27.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdata-validate-ip-perl/libdata-validate-ip-perl_0.27-1.debian.tar.xz
Summary  : 'IPv4 and IPv6 validation methods'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Validate-IP-license
Requires: perl-Data-Validate-IP-man
BuildRequires : perl(NetAddr::IP)
BuildRequires : perl(Test::Requires)

%description
# NAME
Data::Validate::IP - IPv4 and IPv6 validation methods
# VERSION
version 0.27

%package license
Summary: license components for the perl-Data-Validate-IP package.
Group: Default

%description license
license components for the perl-Data-Validate-IP package.


%package man
Summary: man components for the perl-Data-Validate-IP package.
Group: Default

%description man
man components for the perl-Data-Validate-IP package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Data-Validate-IP-0.27
mkdir -p %{_topdir}/BUILD/Data-Validate-IP-0.27/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Data-Validate-IP-0.27/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Data-Validate-IP
cp LICENSE %{buildroot}/usr/share/doc/perl-Data-Validate-IP/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Data/Validate/IP.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Data-Validate-IP/LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Validate::IP.3
