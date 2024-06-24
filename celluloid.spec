Name:           celluloid
Version:        0.27
Release:        1
License:        GPLv3+
Summary:        Media player frontend for MPV based on GTK+, similae to SMPlayer but very simple
URL:            https://github.com/celluloid-player/celluloid/
Source0:        https://github.com/celluloid-player/celluloid/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  appstream-util
BuildRequires:  autoconf2.1
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  intltool >= 0.40.6
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(egl)
# Available in Contrib, so make it recommends. It is optional anyway.
Recommends:     youtube-dl
Requires:       hicolor-icon-theme
Requires:       mpv

Obsoletes:  gnome-mpv

%description
GNOME MPV is a simple GTK+ frontend for mpv. GNOME MPV use mpv library called libmpv,
allowing access to mpv's powerful playback capabilities.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/io.github.celluloid_player.Celluloid.appdata.xml
%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop
%{_datadir}/dbus-1/services/io.github.celluloid_player.Celluloid.service
#{_datadir}/glib-2.0/schemas/io.github.GnomeMpv.gschema.xml
%{_datadir}/glib-2.0/schemas/io.github.celluloid_player.Celluloid.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_mandir}/man1/celluloid.1.*
