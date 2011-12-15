%define major 7
%define libname %mklibname gdata %major
%define develname %mklibname -d gdata %major
%define oname libgdata

Name:           libgdata0.6
Version:        0.6.6
Release:        %mkrel 4
Summary:        Library for the GData protocol

Group:          System/Libraries
License:        LGPLv2+
URL:            http://live.gnome.org/libgdata
Source0: http://ftp.gnome.org/pub/GNOME/sources/%oname/%{oname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  libsoup-devel 
BuildRequires:  dbus-glib-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool

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
Requires: %oname-i18n >= %version

%description -n %{libname}
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.


%package -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:	%name-devel = %version-%release

%description -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x --disable-static
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
%find_lang gdata

#gw remove them manually:
rm -f %buildroot%_libdir/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%check
# Only the general test can be run without network access
cd gdata/tests
#gw this also fails in 0.6.4-4mdv :(
#LD_LIBRARY_PATH=../.libs/ ./general


%files i18n -f gdata.lang

%files -n %libname
%defattr(-,root,root,-)
%doc NEWS README AUTHORS
%{_libdir}/libgdata.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oname}.pc
%{_datadir}/gtk-doc/html/gdata/
