%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	libgdata
%define major	7
%define libname	%mklibname gdata %{major}
%define devname	%mklibname -d gdata %{major}

Summary:	Library for the GData protocol
Name:		libgdata0.6
Version:	0.6.6
Release:	6
Group:		System/Libraries
License:	LGPLv2+
Url:		http://live.gnome.org/libgdata
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/%{url_ver}/%{oname}-%{version}.tar.bz2
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(dbus-glib-1)

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


%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{oname}-%{version}

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

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/gdata/

