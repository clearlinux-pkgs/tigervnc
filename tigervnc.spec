#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tigervnc
Version  : 1.10.1
Release  : 21
URL      : https://github.com/TigerVNC/tigervnc/archive/v1.10.1/tigervnc-1.10.1.tar.gz
Source0  : https://github.com/TigerVNC/tigervnc/archive/v1.10.1/tigervnc-1.10.1.tar.gz
Source1  : ftp://ftp.freedesktop.org/pub/xorg/individual/xserver/xorg-server-1.20.5.tar.bz2
Summary  : A TigerVNC remote display system
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ MIT
Requires: tigervnc-bin = %{version}-%{release}
Requires: tigervnc-data = %{version}-%{release}
Requires: tigervnc-lib = %{version}-%{release}
Requires: tigervnc-license = %{version}-%{release}
Requires: tigervnc-locales = %{version}-%{release}
Requires: tigervnc-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
BuildRequires : cmake
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : flex
BuildRequires : fltk-dev
BuildRequires : font-util-dev
BuildRequires : freetype-dev
BuildRequires : gettext
BuildRequires : gnutls-dev
BuildRequires : graphviz
BuildRequires : libdmx-dev
BuildRequires : libdrm-dev
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
BuildRequires : pkgconfig(gbm)
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
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xau)
BuildRequires : pkgconfig(xcb-aux)
BuildRequires : pkgconfig(xcb-ewmh)
BuildRequires : pkgconfig(xcb-icccm)
BuildRequires : pkgconfig(xcb-image)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xcmiscproto)
BuildRequires : pkgconfig(xdmcp)
BuildRequires : pkgconfig(xf86dgaproto)
BuildRequires : pkgconfig(xf86driproto)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xfont2)
BuildRequires : pkgconfig(xineramaproto)
BuildRequires : pkgconfig(xkbcomp)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xrender)
BuildRequires : pkgconfig(xres)
BuildRequires : pkgconfig(xshmfence)
BuildRequires : pkgconfig(xtst)
BuildRequires : util-macros-dev
BuildRequires : xmlto
BuildRequires : xorgproto-dev
BuildRequires : xtrans-dev
BuildRequires : zlib-dev
Patch1: 0001-stateless-vncserver.patch
Patch2: tigervnc-libvnc-os.patch
Patch3: tigervnc-manpages.patch
Patch4: tigervnc-shebang.patch
Patch5: tigervnc-utilize-system-crypto-policies.patch

%description
Virtual Network Computing (VNC) is a remote display system which
allows you to view a computing 'desktop' environment not only on the
machine where it is running, but from anywhere on the Internet and
from a wide variety of machine architectures.  This package contains a
client which will allow you to connect to other desktops running a VNC
server.

%package bin
Summary: bin components for the tigervnc package.
Group: Binaries
Requires: tigervnc-data = %{version}-%{release}
Requires: tigervnc-license = %{version}-%{release}

%description bin
bin components for the tigervnc package.


%package data
Summary: data components for the tigervnc package.
Group: Data

%description data
data components for the tigervnc package.


%package doc
Summary: doc components for the tigervnc package.
Group: Documentation
Requires: tigervnc-man = %{version}-%{release}

%description doc
doc components for the tigervnc package.


%package extras
Summary: extras components for the tigervnc package.
Group: Default

%description extras
extras components for the tigervnc package.


%package lib
Summary: lib components for the tigervnc package.
Group: Libraries
Requires: tigervnc-data = %{version}-%{release}
Requires: tigervnc-license = %{version}-%{release}

%description lib
lib components for the tigervnc package.


%package license
Summary: license components for the tigervnc package.
Group: Default

%description license
license components for the tigervnc package.


%package locales
Summary: locales components for the tigervnc package.
Group: Default

%description locales
locales components for the tigervnc package.


%package man
Summary: man components for the tigervnc package.
Group: Default

%description man
man components for the tigervnc package.


%prep
%setup -q -n tigervnc-1.10.1
cd %{_builddir}
tar xf %{_sourcedir}/xorg-server-1.20.5.tar.bz2
cd %{_builddir}/tigervnc-1.10.1
mkdir -p unix/xserver2/
cp -r %{_builddir}/xorg-server-1.20.5/* %{_builddir}/tigervnc-1.10.1/unix/xserver2/
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
## build_prepend content
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir}
make V=1 %{?_smp_mflags}

mv unix/xserver unix/xserver-
mv %{_topdir}/BUILD/xorg-server-1.20.5/ unix/xserver/
mv unix/xserver-/hw/vnc unix/xserver/hw/

pushd unix/xserver
patch -p1 < ../xserver120.patch
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
make V=1 %{?_smp_mflags} CFLAGS="${CFLAGS} -I/usr/include/libdrm"
popd
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576891649
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  ||:


%install
export SOURCE_DATE_EPOCH=1576891649
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tigervnc
cp %{_builddir}/tigervnc-1.10.1/LICENCE.TXT %{buildroot}/usr/share/package-licenses/tigervnc/7f7891bc33f6ac443bf927b136696eba605d1d6b
cp %{_builddir}/tigervnc-1.10.1/java/com/jcraft/jsch/LICENSE.txt %{buildroot}/usr/share/package-licenses/tigervnc/3d04bb5917db27f91a65e93cb6b0867f6e029b09
cp %{_builddir}/tigervnc-1.10.1/java/com/jcraft/jzlib/LICENSE.txt %{buildroot}/usr/share/package-licenses/tigervnc/6ccf1d8a00f7c9c080bd538df6fd585d39954596
cp %{_builddir}/tigervnc-1.10.1/java/com/tigervnc/vncviewer/LICENCE.TXT %{buildroot}/usr/share/package-licenses/tigervnc/7f7891bc33f6ac443bf927b136696eba605d1d6b
cp %{_builddir}/tigervnc-1.10.1/unix/xserver2/COPYING %{buildroot}/usr/share/package-licenses/tigervnc/11d1ae389a1a78f7832586e4c2a0c3c7263b7475
%make_install
%find_lang tigervnc
## install_append content
pushd unix/xserver/hw/vnc
make install DESTDIR=%{buildroot}
popd

rm %{buildroot}/usr/lib64/xorg/modules/extensions/libvnc.la
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/Xvnc
/usr/bin/vncconfig
/usr/bin/vncpasswd
/usr/bin/vncviewer
/usr/bin/x0vncserver

%files data
%defattr(-,root,root,-)
/usr/share/applications/vncviewer.desktop
/usr/share/icons/hicolor/16x16/apps/tigervnc.png
/usr/share/icons/hicolor/22x22/apps/tigervnc.png
/usr/share/icons/hicolor/24x24/apps/tigervnc.png
/usr/share/icons/hicolor/32x32/apps/tigervnc.png
/usr/share/icons/hicolor/48x48/apps/tigervnc.png
/usr/share/icons/hicolor/scalable/apps/tigervnc.svg

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/tigervnc/*

%files extras
%defattr(-,root,root,-)
/usr/bin/vncserver

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/extensions/libvnc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tigervnc/11d1ae389a1a78f7832586e4c2a0c3c7263b7475
/usr/share/package-licenses/tigervnc/3d04bb5917db27f91a65e93cb6b0867f6e029b09
/usr/share/package-licenses/tigervnc/6ccf1d8a00f7c9c080bd538df6fd585d39954596
/usr/share/package-licenses/tigervnc/7f7891bc33f6ac443bf927b136696eba605d1d6b

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/Xvnc.1
/usr/share/man/man1/vncconfig.1
/usr/share/man/man1/vncpasswd.1
/usr/share/man/man1/vncserver.1
/usr/share/man/man1/vncviewer.1
/usr/share/man/man1/x0vncserver.1

%files locales -f tigervnc.lang
%defattr(-,root,root,-)

