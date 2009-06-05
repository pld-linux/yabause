Summary:	A Sega Saturn emulator
Summary(pl.UTF-8):	Emulator Segi Saturn
Name:		yabause
Version:	0.9.10
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/yabause/%{name}-%{version}.tar.gz
# Source0-md5:	7e39dd1eb37539d8f24e644fd52a72a7
Patch0:		%{name}-desktop.patch
URL:		http://yabause.org/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtkglext-devel >= 1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yabause is a Sega Saturn emulator under GNU GPL. It currently runs on
FreeBSD, GNU/Linux, Mac OS X and Windows. Yabause support booting
games using Saturn cds or iso files.

%description -l pl.UTF-8
Yabause jest emulatorem Segi Saturn udostępnionym na licencji GPL.
Obecnie działa na systemach FreeBSD, GNU/Linux, Mac OS X i Windows.
Yabause wspiera gry bootowalne używając plików cds oraz iso.

%prep
%setup -q
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
%doc AUTHORS ChangeLog GOALS README README.LIN
%attr(755,root,root) %{_bindir}/*
%{_datadir}/yabause
%{_desktopdir}/yabause.desktop
%{_mandir}/man1/yabause.1*
%{_pixmapsdir}/yabause.png
