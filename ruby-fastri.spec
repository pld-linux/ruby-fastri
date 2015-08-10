%define	pkgname	fastri
Summary:	Fast Ruby documentation browser
Summary(pl.UTF-8):	Szybka przeglądarka dokumentacji Ruby
Name:		ruby-%{pkgname}
Version:	0.3.1
Release:	4
License:	GPL v2
Group:		Development/Languages
Source0:	http://eigenclass.org/static/fastri/%{pkgname}-%{version}.tar.gz
# Source0-md5:	3a7d0a64b1c8e230a34ef7b4bad30dbe
URL:		http://eigenclass.org/hiki.rb?fastri
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FastRI is an alternative to the ri command-line tool. It is *much*
faster, and also allows you to offer RI lookup services over DRb.
FastRI is a bit smarter than ri, and can find classes anywhere in the
hierarchy without specifying the "full path". It also knows about
gems, and can tell you e.g. which extensions to a core class were
added by a specific gem.

%description -l pl.UTF-8
FastRI jest alternatywą dla narzędzia ri. Jest *znacznie* szybszy i
pozwala na oferowanie usług wyszukiwania RI poprzez DRb. FastRI jest
nieco mądrzejszy od ri i może znaleźć klasy gdziekolwiek w hierarchii
bez potrzeby podawania "pełnej ścieżki". Wie także o gemach i może
informować np. o tym które rozszerzenia klasy bazowej zostały dodane
przez określony gem.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
rdoc --ri -o ri lib
rdoc -o rdoc lib
rm -r ri/{DefaultDisplay,Gem,RI}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir},%{_bindir}}

install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
ln -s fri $RPM_BUILD_ROOT%{_bindir}/qri

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.en THANKS
%attr(755,root,root) %{_bindir}/fastri-server
%attr(755,root,root) %{_bindir}/fri
%attr(755,root,root) %{_bindir}/qri
%attr(755,root,root) %{_bindir}/ri-emacs
%{ruby_vendorlibdir}/fastri

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/FastRI
