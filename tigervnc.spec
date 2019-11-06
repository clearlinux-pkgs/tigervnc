Name     : tigervnc
Version  : 1.9.0
Release  : 16
URL      : https://github.com/TigerVNC/tigervnc/archive/v1.9.0.tar.gz
Source0  : https://github.com/TigerVNC/tigervnc/archive/v1.9.0.tar.gz
Source1  : ftp://ftp.freedesktop.org/pub/xorg/individual/xserver/xorg-server-1.20.5.tar.bz2
Summary  : A TigerVNC remote display system
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ MIT
Requires: tigervnc-bin
Requires: tigervnc-doc
Requires: tigervnc-locales

BuildRequires : cmake
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : xorgproto-dev
BuildRequires : flex
BuildRequires : fltk-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : gettext
BuildRequires : graphviz
BuildRequires : libdmx-dev
BuildRequires : libgcrypt-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libtool
BuildRequires : libxshmfence-dev
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : nettle-dev
BuildRequires : pixman-dev
BuildRequires : pkgconfig(bigreqsproto)
BuildRequires : pkgconfig(compositeproto)
BuildRequires : pkgconfig(damageproto)
BuildRequires : pkgconfig(dri2proto)
BuildRequires : pkgconfig(dri3proto)
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(fontsproto)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glproto)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(pixman-1)
BuildRequires : pkgconfig(presentproto)
BuildRequires : pkgconfig(randrproto)
BuildRequires : pkgconfig(recordproto)
BuildRequires : pkgconfig(renderproto)
BuildRequires : pkgconfig(resourceproto)
BuildRequires : pkgconfig(scrnsaverproto)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(videoproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xcmiscproto)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xf86dgaproto)
BuildRequires : pkgconfig(xf86driproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xfont2)
BuildRequires : pkgconfig(xineramaproto)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xres)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xtst)
BuildRequires : util-macros-dev
BuildRequires : xmlto
BuildRequires : xtrans-dev
BuildRequires : zlib-dev



Patch6:     0001-stateless-vncserver.patch
Patch7:     tigervnc-libvnc-os.patch
Patch8:     tigervnc-manpages.patch
Patch10:    tigervnc-shebang.patch
Patch11:    tigervnc-utilize-system-crypto-policies.patch

Patch100:   tigervnc-xserver120.patch

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on thv
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.  This package contains a
client which will allow you to connect to other desktops running a VNC
server.

%package bin
Summary: bin components for the tigervnc package.
Group: Binaries

%description bin
bin components for the tigervnc package.


%package doc
Summary: doc components for the tigervnc package.
Group: Documentation

%description doc
doc components for the tigervnc package.


%package extras
Summary: extras components for the tigervnc package.
Group: Default

%description extras
extras components for the tigervnc package.


%package locales
Summary: locales components for the tigervnc package.
Group: Default

%description locales
locales components for the tigervnc package.


%prep
tar -xf %{SOURCE1}
%setup -q



pushd unix/xserver
cp -r %{_topdir}/BUILD/xorg-server-1.20.5/*  .
%patch100 -p1 -b .xserver120-rebased
popd

%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch11 -p1

%build
export SOURCE_DATE_EPOCH=1484361909

# build breaks if we don't do cmake on TOPDIR
#(e.g: we can't do cmake on clr-build)
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir}
make V=1 %{?_smp_mflags}


pushd unix/xserver
autoreconf -fiv
%configure \
      --disable-present     --enable-dri3        --disable-dmx         \
      --disable-static      --disable-dri        --disable-xorg        \
      --disable-xnest       --disable-xvfb       --disable-xwin        \
      --disable-xephyr      --disable-kdrive     --disable-config-dbus \
      --disable-config-hal  --disable-config-udev                      \
      --without-dtrace      --enable-dri2        --disable-glx         \
      --enable-glx-tls      --with-pic           --disable-xwayland    \
      --disable-selective-werror                 --disable-unit-tests  \
      --disable-devel-docs  --enable-glx         --with-fontrootdir=/usr/share/fonts/X11
make V=1 %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1484361909
rm -rf %{buildroot}
%make_install

pushd unix/xserver/hw/vnc
make install DESTDIR=%{buildroot}
popd

%find_lang tigervnc

%files
%defattr(-,root,root,-)
/usr/share/applications/vncviewer.desktop
/usr/share/icons/hicolor/16x16/apps/tigervnc.png
/usr/share/icons/hicolor/22x22/apps/tigervnc.png
/usr/share/icons/hicolor/24x24/apps/tigervnc.png
/usr/share/icons/hicolor/32x32/apps/tigervnc.png
/usr/share/icons/hicolor/48x48/apps/tigervnc.png
/usr/share/icons/hicolor/scalable/apps/tigervnc.svg

%files bin
%defattr(-,root,root,-)
/usr/bin/Xvnc
/usr/bin/vncconfig
/usr/bin/vncpasswd
/usr/bin/vncviewer
/usr/bin/x0vncserver

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/tigervnc/*
%doc /usr/share/man/man1/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/extensions/libvnc.so
/usr/bin/vncserver
%exclude /usr/lib64/xorg/modules/extensions/libvnc.la

%files locales -f tigervnc.lang
%defattr(-,root,root,-)
