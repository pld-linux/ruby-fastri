Summary:	Fast Ruby documentation browser
Summary(pl.UTF-8):	Szybka przeglądarka dokumentacji Ruby
Name:		ruby-fastri
Version:	0.2.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/14948/fastri-%{version}.tar.gz
# Source0-md5:	059a6f1c9b3b6dd805b2b650dc1bd73b
URL:		http://eigenclass.org/hiki.rb?fastri
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FastRI is an alternative to the ri command-line tool. It is *much*
faster, and also allows you to offer RI lookup services over DRb.
FastRI is a bit smarter than ri, and can find classes anywhere in
the hierarchy without specifying the "full path". It also knows
about gems, and can tell you e.g. which extensions to a core class
were added by a specific gem.

%description -l pl.UTF-8
FastRI jest alternatywą dla narzędzia ri. Jest *znacznie* szybszy i
pozwala na oferowanie usług wyszukiwania RI poprzez DRb. FastRI jest
nieco mądrzejszy od ri i może znaleźć klasy gdziekolwiek w hierarchii
bez potrzeby podawania "pełnej ścieżki". Wie także o gemach i może
informować np. o tym które rozszerzenia klasy bazowej zostały dodane
przez określony gem.

%prep
%setup -q -n fastri-%{version}

%build

ruby setup.rb config \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

rdoc --ri -o ri lib
rdoc -o rdoc lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_archdir}
install -d $RPM_BUILD_ROOT%{ruby_ridir}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fastri-server
%attr(755,root,root) %{_bindir}/fri
%attr(755,root,root) %{_bindir}/ri-emacs
%{ruby_rubylibdir}/fastri
