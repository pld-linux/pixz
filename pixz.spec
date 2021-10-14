# TODO
# - fill proper gcc BR for -pie
Summary:	A parallel, indexing version of XZ
Name:		pixz
Version:	1.0.7
Release:	1
License:	BSD-2-Clause
Group:		Applications/Archiving
Source0:	https://github.com/vasi/pixz/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	06fcda5892dfad818fe45e8e63427134
URL:		https://github.com/vasi/pixz
BuildRequires:	libarchive-devel
BuildRequires:	openssl-devel
BuildRequires:	rpmbuild(macros)
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pixz (pronounced 'pixie') is a parallel, indexing version of XZ

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md NEWS
%attr(755,root,root) %{_bindir}/pixz
%{_mandir}/man1/pixz.1*
