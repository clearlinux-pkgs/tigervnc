Name     : tigervnc
Version  : 1.6.0
Release  : 3
URL      : https://github.com/TigerVNC/tigervnc/archive/v1.6.0.tar.gz
Source0  : https://github.com/TigerVNC/tigervnc/archive/v1.6.0.tar.gz
Source1  : ftp://ftp.freedesktop.org/pub/xorg/individual/xserver/xorg-server-1.18.4.tar.bz2
Summary  : A TigerVNC remote display system
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ MIT
Requires: tigervnc-bin
Requires: tigervnc-doc
Requires: tigervnc-locales

BuildRequires : cmake
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : dri2proto-dev
BuildRequires : dri3proto-dev
BuildRequires : flex
BuildRequires : fltk-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : gettext
BuildRequires : glproto-dev
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
BuildRequires : pkgconfig(xfont)
BuildRequires : pkgconfig(xineramaproto)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xres)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : util-macros-dev
BuildRequires : xmlto
BuildRequires : xtrans-dev
BuildRequires : zlib-dev

Patch1:  0001-stateless-vncserver.patch
Patch2:  tigervnc-cookie.patch
Patch3:  tigervnc-libvnc-os.patch
Patch4:  tigervnc11-rh692048.patch
Patch5:  tigervnc-inetd-nowait.patch
Patch6:  tigervnc-manpages.patch
Patch7:  tigervnc-getmaster.patch
Patch8:  tigervnc-shebang.patch
Patch9:  tigervnc-xserver118.patch
Patch10: tigervnc-xorg118-QueueKeyboardEvents.patch
Patch11: tigervnc-utilize-system-crypto-policies.patch

Patch100: tigervnc-xserver116-rebased.patch

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
%setup -q -n tigervnc-1.6.0

pushd unix/xserver
cp -r %{_topdir}/BUILD/xorg-server-1.18.4/*  .
%patch100 -p1 -b .xserver116-rebased
popd

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
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
rm -rf %{buildroot}
%make_install

pushd unix/xserver/hw/vnc
make install DESTDIR=%{buildroot}
popd

%find_lang tigervnc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/Xvnc
/usr/bin/vncconfig
/usr/bin/vncpasswd
/usr/bin/vncserver
/usr/bin/vncviewer
/usr/bin/x0vncserver

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/tigervnc/*
%doc /usr/share/man/man1/*

%files extras
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/extensions/libvnc.so
%exclude /usr/lib64/xorg/modules/extensions/libvnc.la

%files locales -f tigervnc.lang
%defattr(-,root,root,-)
