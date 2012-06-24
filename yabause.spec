Summary:	A Sega Saturn emulator
Summary(pl):	Emulator Segi Saturn
Name:		yabause
Version:	0.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/yabause/%{name}-%{version}.tar.gz
# Source0-md5:	f61c3829b3505691b151fb77d08fd183
Patch0:		%{name}-desktop.patch
URL:		http://yabause.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	freetype-devel
BuildRequires:	glut-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yabause is a Sega Saturn emulator under GNU GPL. It currently runs on
FreeBSD, GNU/Linux, Mac OS X and Windows. Yabause support booting
games using Saturn cds or iso files.

%description -l pl
Yabause jest emulatorem Segi Saturn opartym na licencji GPL. Obecnie
jest on dost�pny dla FreeBSD, GNU/Linux, Mac OS X i Windows. Yabause
wspiera gry bootowalne u�ywaj�c plik�w cds oraz iso.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog GOALS README README.LIN TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_mandir}/man1/**
%{_pixmapsdir}/%{name}.png
