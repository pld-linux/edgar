Summary:	2D Platform game
Summary(pl.UTF-8):	Dwuwymiarowa gra platformowa
Name:		edgar
Version:	0.56
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.parallelrealities.co.uk/download/edgar/%{name}-%{version}-1.tar.gz
# Source0-md5:	b09ee1a313a61c59386d0091abe28d95
Source1:	%{name}.png
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-usless_files.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.parallelrealities.co.uk/projects/edgar.php
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	gettext-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In The Legend of Edgar you take on the role of Edgar as he ventures
across the world, battling fearsome creatures and solving puzzles
whilst trying to find and rescue his father.

%description -l pl.UTF-8
W The Legend of Edgar gracz wciela się w rolę Edgara podróżując przez
świat, walcząc z przerażającymi potworami i rozwiązując zagadki
podczas próby odnalezienia i uratowania swojego ojca.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CXX="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/edgar
%{_datadir}/edgar
%{_desktopdir}/edgar.desktop
%{_pixmapsdir}/edgar.png
