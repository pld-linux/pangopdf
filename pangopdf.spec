Summary:	Pango PDF backend
Summary(pl):	Backend PDF dla Pango
Name:		pangopdf
Version:	1.2.0.1
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://pangopdf.sourceforge.net/
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

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
