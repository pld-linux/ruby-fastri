#
# Conditional build:
%bcond_without	docs # don't generate & install documentation (most timeconsuming)
%define		_name	fastri
Summary:	Fast Ruby documentation browser
Summary(pl.UTF-8):	Szybka przeglądarka dokumentacji Ruby
Name:		ruby-%{_name}
Version:	0.3.1
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://eigenclass.org/static/fastri/%{_name}-%{version}.tar.gz	
# Source0-md5:	3a7d0a64b1c8e230a34ef7b4bad30dbe
URL:		http://eigenclass.org/hiki.rb?fastri
%{?ruby_mod_ver_requires_eq}
Requires:	ruby-modules >= 1:1.8.7-3
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
%setup -q -n %{_name}-%{version}

%build
%{__ruby} setup.rb config \
	--site-ruby=%{ruby_vendorlibdir} \
	--so-dir=%{ruby_vendorarchdir}
ruby setup.rb setup

%if %{with docs}
rdoc --ri -o ri lib
rdoc -o rdoc lib
%endif

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%if %{with docs}
#install -d $RPM_BUILD_ROOT%{ruby_ridir} <- now it points to `/usr/share/ri/1.8/system', should to /usr/share/ri/1.8
install -d $RPM_BUILD_ROOT%{_datadir}/ri/%{ruby_version}/site # should be `vendor' instead of `site'? ri/fastri supports looking into `vendor' subdir? 
rm -f {ri,rdoc}/created.rid
cp -fR ri/* $RPM_BUILD_ROOT%{_datadir}/ri/%{ruby_version}/site
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES README.en THANKS %{?with_docs:rdoc/*}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fastri-server
%attr(755,root,root) %{_bindir}/fri
%attr(755,root,root) %{_bindir}/qri
%attr(755,root,root) %{_bindir}/ri-emacs
%{ruby_vendorlibdir}/fastri
%dir %{?with_docs:%{_datadir}/ri/%{ruby_version}/site}
%{?with_docs:%{_datadir}/ri/%{ruby_version}/site/*}
