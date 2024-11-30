#
# Conditional build:
%bcond_with	ffmpeg	# MPEG support via FFmpeg (< 5)
%bcond_without	gtk	# GTK+ (2.x) port
%bcond_without	qt	# Qt (5.x) port

Summary:	A Sega Saturn emulator
Summary(pl.UTF-8):	Emulator Segi Saturn
Name:		yabause
Version:	0.9.15
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
#Source0Download: https://yabause.org/download/
Source0:	https://download.tuxfamily.org/yabause/releases/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	efcf00e038ec24c8310285f87e61d579
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-cmake.patch
Patch2:		%{name}-lodepng.patch
Patch3:		%{name}-qt5.patch
Patch4:		%{name}-musashi.patch
URL:		http://yabause.org/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-glut-devel
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Multimedia-devel >= 5
BuildRequires:	Qt5OpenGL-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
%endif
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	cmake >= 2.8
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel < 5}
%{?with_gtk:BuildRequires:	gdk-pixbuf2-devel >= 2.0}
BuildRequires:	glew-devel
%{?with_gtk:BuildRequires:	gtk+2-devel >= 2:2.10}
%{?with_gtk:BuildRequires:	gtkglext-devel >= 1.0}
BuildRequires:	libstdc++-devel
BuildRequires:	lodepng-devel
BuildRequires:	mini18n-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
%if %{with qt}
BuildRequires:	qt5-build >= 5
%endif
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
Provides:	%{name}-engine = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yabause is a Sega Saturn emulator under GNU GPL. It currently runs on
FreeBSD, GNU/Linux, Mac OS X and Windows. Yabause support booting
games using Saturn cds or iso files.

This package contains GTK+ port of emulator.

%description -l pl.UTF-8
Yabause jest emulatorem Segi Saturn udostępnionym na licencji GPL.
Obecnie działa na systemach FreeBSD, GNU/Linux, Mac OS X i Windows.
Yabause wspiera gry bootowalne używając plików cds oraz iso.

Ten pakiet zawiera wersję GTK+ emulatora.

%package qt
Summary:	A Sega Saturn emulator
Summary(pl.UTF-8):	Emulator Segi Saturn
Group:		X11/Applications/Games
Requires:	%{name}-data = %{version}-%{release}
Provides:	%{name}-engine = %{version}-%{release}

%description qt
Yabause is a Sega Saturn emulator under GNU GPL. It currently runs on
FreeBSD, GNU/Linux, Mac OS X and Windows. Yabause support booting
games using Saturn cds or iso files.

This package contains GTK+ port of emulator.

%description qt -l pl.UTF-8
Yabause jest emulatorem Segi Saturn udostępnionym na licencji GPL.
Obecnie działa na systemach FreeBSD, GNU/Linux, Mac OS X i Windows.
Yabause wspiera gry bootowalne używając plików cds oraz iso.

Ten pakiet zawiera wersję GTK+ emulatora.

%package data
Summary:	Data for Yabause Sega Saturn emulator
Summary(pl.UTF-8):	Dane dla Yabause - emulatora Segi Saturn
Group:		X11/Applications/Games
Requires:	%{name}-engine = %{version}-%{release}
BuildArch:	noarch

%description data
Data for Yabause - Sega Saturn emulator.

%description data -l pl
Dane dla Yabause - emulatora Segi Saturn.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_ASM-ATT_COMPILER=as \
	-DYAB_MULTIBUILD=ON \
	-DYAB_NETWORK=ON \
	-DYAB_OPTIMIZATION="" \
	-DYAB_PORTS="%{?with_gtk:gtk;}%{?with_qt:qt;}runner" \
	-DYAB_USE_SCSPMIDI=ON \
	%{?with_ffmpeg:-DYAB_WANT_MPEG=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# unify to short code
%{__mv} $RPM_BUILD_ROOT%{_datadir}/yabause/yts/{pl_PL,pl}.yts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/yabause-gtk
%{_desktopdir}/yabause-gtk.desktop
%{_mandir}/man1/yabause-gtk.1*

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yabause-qt
%{_desktopdir}/yabause-qt.desktop
%{_mandir}/man1/yabause-qt.1*

%files data
%defattr(644,root,root,755)
%dir %{_datadir}/yabause
%dir %{_datadir}/yabause/yts
%lang(ar) %{_datadir}/yabause/yts/ar.yts
%lang(da) %{_datadir}/yabause/yts/da.yts
%lang(de) %{_datadir}/yabause/yts/de.yts
%lang(el) %{_datadir}/yabause/yts/el.yts
%lang(es) %{_datadir}/yabause/yts/es.yts
%lang(fr) %{_datadir}/yabause/yts/fr.yts
%lang(it) %{_datadir}/yabause/yts/it.yts
%lang(ja) %{_datadir}/yabause/yts/ja.yts
%lang(ko) %{_datadir}/yabause/yts/ko.yts
%lang(lt) %{_datadir}/yabause/yts/lt.yts
%lang(nl) %{_datadir}/yabause/yts/nl.yts
%lang(pl) %{_datadir}/yabause/yts/pl.yts
%lang(pt) %{_datadir}/yabause/yts/pt.yts
%lang(pt_BR) %{_datadir}/yabause/yts/pt_BR.yts
%lang(ru) %{_datadir}/yabause/yts/ru.yts
%lang(sv) %{_datadir}/yabause/yts/sv.yts
%lang(tr) %{_datadir}/yabause/yts/tr.yts
%lang(zh_CN) %{_datadir}/yabause/yts/zh_CN.yts
%lang(zh_TW) %{_datadir}/yabause/yts/zh_TW.yts
%{_pixmapsdir}/yabause.png
