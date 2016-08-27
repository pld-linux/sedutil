# TODO:	build PBAs
Summary:	Self encrypting drive software
Name:		sedutil
Version:	1.12
Release:	1
License:	GPL v3+
Group:		Applications/System
Source0:	https://github.com/Drive-Trust-Alliance/sedutil/archive/%{version}.tar.gz
# Source0-md5:	ea8c3c6ae806a00feb292c6970f93e09
# https://github.com/JanLuca/sedutil/commit/44e144ae2b85dc541bd09945311a2030ab412e98.patch
Patch0:		44e144ae2b85dc541bd09945311a2030ab412e98.patch
URL:		https://github.com/Drive-Trust-Alliance/sedutil
BuildRequires:	libstdc++-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Drive Trust Alliance Self Encrypting Drive Utility.

This program and it's accompanying Pre-Boot Authorization image allow
you to enable the locking in SED's that comply with the TCG OPAL 2.00
standard on BIOS machines.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C linux/CLI \
%ifarch %{x8664}
	CONF=Release_x86_64
%else
	CONF=Release_i686
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install linux/CLI/dist/Release_*/GNU-Linux/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{name}
