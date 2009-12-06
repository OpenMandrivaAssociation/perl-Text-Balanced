%define upstream_name    Text-Balanced
%define upstream_version 2.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extract balanced-delimiter substrings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The various 'extract_...' subroutines may be used to extract a delimited
substring, possibly after skipping a specified prefix string. By default,
that prefix is optional whitespace ('/\s*/'), but you can change it to
whatever you wish (see below).

The substring to be extracted must appear at the current 'pos' location of
the string's variable (or at index zero, if no 'pos' position is defined).
In other words, the 'extract_...' subroutines _don't_ extract the first
occurrence of a substring anywhere in a string (like an unanchored regex
would). Rather, they extract an occurrence of the substring appearing
immediately at the current matching position in the string (like a
'\G'-anchored regex would).

General behaviour in list contexts
    In a list context, all the subroutines return a list, the first three
    elements of which are always:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


