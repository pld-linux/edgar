Summary:	2D Platform game
Summary(pl.UTF-8):	Dwuwymiarowa gra platformowa
Name:		edgar
Version:	0.97
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/legendofedgar/%{name}-%{version}-1.tar.gz
# Source0-md5:	b9a1c89da2ebeab2fff0a1a79ae7cb08
Source1:	%{name}.png
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-useless_files.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.parallelrealities.co.uk/p/legend-of-edgar.html
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	gettext-tools
BuildRequires:	zlib-devel
Requires:	audiofile
Requires:	libmikmod
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
%{_datadir}/games/edgar
%{_desktopdir}/edgar.desktop
%{_pixmapsdir}/edgar.png
