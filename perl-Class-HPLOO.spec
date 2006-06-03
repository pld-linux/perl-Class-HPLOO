#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	HPLOO
Summary:	Declare classes basing on the popular class {...} style and ePod
Summary(pl):	Deklarowanie klas opartych na popularnym stylu klas {...} i ePod
Name:		perl-Class-HPLOO
Version:	0.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	430ba4c8cac1091196797daa82d3f3fb
URL:		http://search.cpan.org/dist/Class-HPLOO/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the implemantation of OO-Classes for HPL. This brings an easy
way to create PM classes, but with HPL resources/style.

%description -l pl
To jest implementacja klas zorientowanych obiektowo (OO-Classes) dla
HPL-a. Udostêpnia ³atwy sposób tworzenia klas PM, ale w stylu zasobów
HPL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc Changes README
%{perl_vendorlib}/Class/*.pm
%{perl_vendorlib}/Class/HPLOO
%{_mandir}/man3/*
