%define major 7
%define libname %mklibname gdata %{major}
%define develname %mklibname -d gdata %{major}
%define oname libgdata

Name:		libgdata0.6
Version:	0.6.6
Release:	6
Summary:	Library for the GData protocol

Group:		System/Libraries
License:	LGPLv2+
URL:		http://live.gnome.org/libgdata
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%oname/%{oname}-%{version}.tar.bz2

BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package i18n
Summary:	Library for the GData protocol - translations
Group:		System/Internationalization

%description i18n
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package -n %{libname}
Summary:	Library for the GData protocol
Group:		System/Libraries
Suggests:	%{oname}-i18n >= %{version}

%description -n %{libname}
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.


%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
%find_lang gdata

%files i18n -f gdata.lang

%files -n %{libname}
%doc NEWS README AUTHORS
%{_libdir}/libgdata.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/gdata/


%changelog
* Thu Dec 15 2011 Götz Waschk <waschk@mandriva.org> 0.6.6-5mdv2012.0
+ Revision: 741476
- really remove libtool archives
- fork out old version of libgdata
- remove libtool and gir support
- update to new version 0.6.6
- update to new version 0.6.5
- rebuild for new g-i
- disable check
- rebuild for new libproxy
- update to new version 0.6.4
- update to new version 0.6.3
- update to new version 0.6.2
- update to new version 0.6.1
- new version
- new major
- add gobject-introspection support
- update to new version 0.5.1
- new version
- new major
- new version
- new major
- fix build deps
- new version
- new major
- fix check
- fix devel provides
- import libgdata

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 0.6.6
      release: 3
      revision: 662368
      Copying 0.6.6-3 to releases/ directory.

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - rebuild for updated libsoup libtool archive
    - rebuild for new gobject-introspection

