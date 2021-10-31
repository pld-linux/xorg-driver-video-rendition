Summary:	X.org video driver for Rendition/Micron video chips
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów graficznych Rendition/Micron
Name:		xorg-driver-video-rendition
Version:	4.2.7
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-rendition-%{version}.tar.bz2
# Source0-md5:	d21c65b68b74206a67ecc54ec0589a7c
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.0.99.901
Provides:	xorg-driver-video
Obsoletes:	X11-driver-rendition < 1:7.0.0
Obsoletes:	XFree86-Rendition
Obsoletes:	XFree86-driver-rendition < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautostrip	.*.uc

%description
X.org video driver for Rendition/Micron video chips. It supports PCI
and AGP video cards based on the following chips: Verite V1000, Verite
V2100, Verite V2200.

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów graficznych Rendition/Micron.
Obsługuje karty PCI i AGP oparte na następujących układach: Verite
V1000, Verite V2100, Verite V2200.

%prep
%setup -q -n xf86-video-rendition-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/rendition_drv.so
%{_libdir}/xorg/modules/v10002d.uc
%{_libdir}/xorg/modules/v20002d.uc
%{_mandir}/man4/rendition.4*
