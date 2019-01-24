
Name:           gnome-mpv
Version:        0.16
Release:        1
License:        GPLv3+
Summary:        Media player frontend for MPV based on GTK+, similae to SMPlayer but very simple
URL:            https://github.com/gnome-mpv/gnome-mpv
Source0:        https://github.com/gnome-mpv/gnome-mpv/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf2.1
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  intltool >= 0.40.6
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(egl)
Requires:       youtube-dl
Requires:       hicolor-icon-theme

%description
GNOME MPV is a simple GTK+ frontend for mpv. GNOME MPV use mpv library called libmpv,
allowing access to mpv's powerful playback capabilities.

%prep
%autosetup

%build
%configure
%make_build V=1

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/io.github.GnomeMpv.appdata.xml
%{_datadir}/applications/io.github.GnomeMpv.desktop
%{_datadir}/dbus-1/services/io.github.GnomeMpv.service
%{_datadir}/glib-2.0/schemas/io.github.GnomeMpv.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome-mpv.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/gnome-mpv.1.xz
