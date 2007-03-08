Summary:	Fast Ruby documentation browser
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
Fast Ruby documentation browser

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
