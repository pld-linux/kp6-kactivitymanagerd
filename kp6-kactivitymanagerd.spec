#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.0.3
%define		qtver		5.15.2
%define		kpname		kactivitymanagerd
Summary:	kactivitymanagerd
Name:		kp6-%{kpname}
Version:	6.0.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	52d84e5435c807851e91b31e724b0c2a
URL:		http://www.kde.org/
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Sql-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	boost-devel
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-kdoctools-devel
BuildRequires:	kf6-kglobalaccel-devel
BuildRequires:	kf6-kwindowsystem-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-qmake
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System service to manage user's activities, track the usage patterns
etc.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/kactivitymanagerd
%attr(755,root,root) %{_libdir}/libkactivitymanagerd_plugin.so
%dir %{_libdir}/qt6/plugins/kactivitymanagerd1
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.ActivityRunner.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.ActivityTemplates.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.GlobalShortcuts.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.LibreOfficeEventSpy.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.RecentlyUsedEventSpy.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.ResourceScoring.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.RunApplication.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kactivitymanagerd1/org.kde.ActivityManager.VirtualDesktopSwitch.so
%{systemduserunitdir}/plasma-kactivitymanagerd.service
%{_datadir}/dbus-1/services/org.kde.ActivityManager.service
%{_datadir}/qlogging-categories6/kactivitymanagerd.categories
%{_datadir}/krunner/dbusplugins/plasma-runnners-activities.desktop
