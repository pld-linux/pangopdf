#
# Conditional build:
%bcond_with	gnomeprint	# build GNOME Print (pangogp) backend
				# (broken: libgnomeprint is linked with newer pango)
%bcond_without	qt		# don't build Qt-based viewer
#
Summary:	Pango PDF backend
Summary(pl.UTF-8):	Backend PDF dla Pango
Name:		pangopdf
Version:	1.2.3.7
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/pangopdf/%{name}-%{version}.tar.gz
# Source0-md5:	e0671aeaba45e0aa5a2c1aba8cebba41
URL:		http://pangopdf.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	fontconfig-devel >= 1:1.0.1
BuildRequires:	glib2-devel >= 2.1.3
BuildRequires:	gtk-doc >= 0.10
%{?with_gnomeprint:BuildRequires:	libgnomeprint-devel >= 2.2}
%{?with_qt:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pdflib-devel >= 4.0.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt-devel}
BuildRequires:	xft-devel >= 2.0.0
Requires:	glib2-devel >= 2.1.3
Requires:	fontconfig >= 1:1.0.1
Requires:	freetype >= 2.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	libpango-1.0.so.0 libpangoft2-1.0.so.0 libpangox-1.0.so.0 libpangoxft-1.0.so.0

%description
PangoPDF implements a version of the Pango (http://www.pango.org/)
library with a PDF backend for creating PDF output. This library also
implements several of the inline properties defined by XSL
(http://www.w3.org/TR/xsl/) that are not currently implemented by
Pango.

%description -l pl.UTF-8
PangoPDF to implementacja wersji biblioteki Pango
(http://www.pango.org/) z backendem PDF do tworzenia wyjścia w PDF. Ta
biblioteka ma zaimplementowanych także trochę własności inline
zdefiniowanych przez XSL (http://www.w3.org/TR/xsl/), które aktualnie
nie są zaimplementowane w Pango.

%package devel
Summary:	Header files for Pango PDF backend
Summary(pl.UTF-8):	Pliki nagłówkowe dla backendu PDF dla Pango
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
PangoPDF implements a version of the Pango (http://www.pango.org/)
library with a PDF backend for creating PDF output. This library also
implements several of the inline properties defined by XSL
(http://www.w3.org/TR/xsl/) that are not currently implemented by
Pango.

This package contains the header files needed to develop programs that
use these pangopdf.

%description devel -l pl.UTF-8
PangoPDF to implementacja wersji biblioteki Pango
(http://www.pango.org/) z backendem PDF do tworzenia wyjścia w PDF. Ta
biblioteka ma zaimplementowanych także trochę własności inline
zdefiniowanych przez XSL (http://www.w3.org/TR/xsl/), które aktualnie
nie są zaimplementowane w Pango.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających bibliotek pangopdf.

%package viewer
Summary:	pangopdf and Qt based UTF-8 file viewer
Summary(pl.UTF-8):	Przeglądarka plików UTF-8 oparta na pangopdf i Qt
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description viewer
Example program to view a UTF-8 encoding file using Pango to render
result.

%description viewer -l pl.UTF-8
Przykładowy program do oglądania plików w kodowaniu UTF-8 przy użyciu
Pango do wyświetlania wyników.

%prep
%setup -q

sed -i -e 's,QTDIR/lib ,QTDIR/%{_lib} ,;s,QTDIR/include,QTDIR/include/qt,;s/-lqt/-lqt-mt/' \
	configure.in
sed -i -e 's,QTDIR)/lib ,QTDIR)/%{_lib} ,;s,QTDIR)/include,QTDIR)/include/qt,;s/-lqt/-lqt-mt/' \
	examples/Makefile.am

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gnomeprint:--disable-gp} \
	--enable-pdflib \
	--with-html-dir=%{_gtkdocdir} \
	--with-x \
	--with%{!?with_qt:out}-qt%{?with_qt:=/usr}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/pangopdf/pango/1.2.0/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS* ChangeLog* NEWS* README* TODO
%attr(755,root,root) %{_bindir}/pangopdf-querymodules
%dir %{_sysconfdir}/pangopdf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pangopdf/pangox.aliases
%dir %{_libdir}/pangopdf
%attr(755,root,root) %{_libdir}/pangopdf/lib*.so.*
%dir %{_libdir}/pangopdf/pango
%dir %{_libdir}/pangopdf/pango/1.2.0
%dir %{_libdir}/pangopdf/pango/1.2.0/modules
%attr(755,root,root) %{_libdir}/pangopdf/pango/1.2.0/modules/*.so
%{_datadir}/pangopdf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/pangopdf/*.so
%{_libdir}/pangopdf/*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/pangopdf
%{_gtkdocdir}/pangopdf

%if %{with qt}
%files viewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pango-viewer
%endif
