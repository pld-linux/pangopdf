Summary:	Pango PDF backend
Summary(pl):	Backend PDF dla Pango
Name:		pangopdf
Version:	1.2.1.1
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	04c2cc8247b4cb5779b87f8c7f66b1f6
URL:		http://pangopdf.sourceforge.net/
BuildRequires:	freetype-devel >= 2.0.9
BuildRequires:	fontconfig-devel >= 1.0.1
BuildRequires:	glib2-devel >= 2.1.3
BuildRequires:	gtk-doc >= 0.10
BuildRequires:	libgnomeprint-devel >= 2.2
BuildRequires:	pdflib-devel >= 4.0.0
BuildRequires:	pkgconfig
BuildRequires:	xft-devel >= 2.0.0
Requires:	glib2-devel >= 2.1.3
Requires:	fontconfig >= 1.0.1
Requires:	freetype >= 2.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PangoPDF implements a version of the Pango (http://www.pango.org/)
library with a PDF backend for creating PDF output. This library also
implements several of the inline properties defined by XSL
(http://www.w3.org/TR/xsl/) that are not currently implemented by
Pango.

%description -l pl
PangoPDF to implementacja wersji biblioteki Pango
(http://www.pango.org/) z backendem PDF do tworzenia wyj¶cia w PDF. Ta
biblioteka ma zaimplementowanych tak¿e trochê w³asno¶ci inline
zdefiniowanych przez XSL (http://www.w3.org/TR/xsl/), które aktualnie
nie s± zaimplementowane w Pango.

%package devel
Summary:	Header files for Pango PDF backend
Summary(pl):	Pliki nag³ówkowe dla backendu PDF dla Pango
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
PangoPDF implements a version of the Pango (http://www.pango.org/)
library with a PDF backend for creating PDF output. This library also
implements several of the inline properties defined by XSL
(http://www.w3.org/TR/xsl/) that are not currently implemented by
Pango.

This package contains the header files needed to develop programs that
use these pangopdf.

%description devel -l pl
PangoPDF to implementacja wersji biblioteki Pango
(http://www.pango.org/) z backendem PDF do tworzenia wyj¶cia w PDF. Ta
biblioteka ma zaimplementowanych tak¿e trochê w³asno¶ci inline
zdefiniowanych przez XSL (http://www.w3.org/TR/xsl/), które aktualnie
nie s± zaimplementowane w Pango.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych bibliotek pangopdf.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig -n /usr/lib/pangopdf

%files
%defattr(644,root,root,755)
%doc ChangeLog README
#%%attr(755,root,root) %{_bindir}/*
#%%config %{_sysconfdir}/pango/pangox.aliases
%attr(755,root,root) %{_libdir}/pangopdf/lib*.so.*.*
%dir %{_libdir}/pangopdf/pango
%dir %{_libdir}/pangopdf/pango/1.2.0
%dir %{_libdir}/pangopdf/pango/1.2.0/modules
%attr(755,root,root) %{_libdir}/pangopdf/pango/1.2.0/modules/*.so
%{_libdir}/pangopdf/pango/1.2.0/modules/*.la
%{_datadir}/pangopdf

%files devel
%defattr(644,root,root,755)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangopdf/*.la
%{_libdir}/pangopdf/*.so
%{_includedir}/pangopdf
%{_gtkdocdir}/pangopdf
