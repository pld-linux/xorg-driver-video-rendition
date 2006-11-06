Summary:	X.org video driver for Rendition/Micron video chips
Summary(pl):	Sterownik obrazu X.org dla uk³adów graficznych Rendition/Micron
Name:		xorg-driver-video-rendition
Version:	4.1.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-rendition-%{version}.tar.bz2
# Source0-md5:	a0d2fb2d4a5d75b65d033a318e3a9798
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for Rendition/Micron video chips. It supports PCI
and AGP video cards based on the following chips: Verite V1000, Verite
V2100, Verite V2200.

%description -l pl
Sterownik obrazu X.org dla uk³adów graficznych Rendition/Micron.
Obs³uguje karty PCI i AGP oparte na nastêpuj±cych uk³adach: Verite
V1000, Verite V2100, Verite V2200.

%prep
%setup -q -n xf86-video-rendition-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/rendition_drv.so
%{_libdir}/xorg/modules/v10002d.uc
%{_libdir}/xorg/modules/v20002d.uc
%{_mandir}/man4/rendition.4*
