# TODO
# - fill proper gcc BR for -pie
Summary:	A parallel, indexing version of XZ
Name:		pixz
Version:	1.0.2
Release:	1
License:	BSD-2-Clause
Group:		Applications/Archiving
Source0:	http://downloads.sourceforge.net/pixz/%{name}-%{version}.tgz
# Source0-md5:	90034c862d7c9340b76611f3fb909855
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
export LDFLAGS="$LDFLAGS -lm -lcrypto -pie"
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p pixz $RPM_BUILD_ROOT/%{_bindir}
cp -p pixz.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/pixz
%{_mandir}/man1/pixz.1*
