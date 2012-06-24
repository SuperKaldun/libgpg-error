Summary:	Library libgpg-error
Summary(pl):	Biblioteka libgpg-error
Name:		libgpg-error
Version:	0.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libgpg-error/%{name}-%{version}.tar.gz
# Source0-md5:	b82fd5a0874b0149ade1de327a3b0b9d
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

%description -l pl
libgpg-error jest bibliotek� definiuj�c� warto�ci b��d�w wsp�lne dla
komponent�w GnuPG. S� w�r�d nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przysz�o�ci.

%package devel
Summary:	Header files for %{name}
Summary(pl):	Pliki nag��wkowe dla %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

This package contains the header files needed to develop programs that
use these libgpg-error

%description devel -l pl
libgpg-error jest bibliotek� definiuj�c� warto�ci b��d�w wsp�lne dla
komponent�w GnuPG. S� w�r�d nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przysz�o�ci.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libgpg-error.

%package static
Summary:	Static version of %{name} library
Summary(pl):	Statyczna wersja biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

This package contains the static libgpg-error libraries.

%description static -l pl
libgpg-error jest bibliotek� definiuj�c� warto�ci b��d�w wsp�lne dla
komponent�w GnuPG. S� w�r�d nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przysz�o�ci.

Pakiet zawiera statyczne biblioteki libgpg-error.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-error-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
