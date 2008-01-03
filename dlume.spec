%define rel 3
%define	name	dlume
%define	version	0.2.4
%define	release	%mkrel %{rel}
%define Summary	An easy to use address book

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://clay.ll.pl/download/%{name}-%{version}.tar.bz2
URL:		http://clay.ll.pl/dlume.html
License:	GPL
Group:		Office
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libxml2-devel >= 2.4.0 ImageMagick

%description
Dlume is nice, Gtk 2-based address book. 
You can easily add, edit, and delete records from an XML database.
A Quick-search makes it easy to find entries.
Exporting to CSV and HTML formats is also possible.

%prep
%setup -q

%build 
%configure2_5x --enable-nls
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%find_lang %{name}

#icons and menu 
mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
install -m 644 dlume.png %{buildroot}%{_iconsdir}/%{name}.png
convert dlume.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{name}.png
convert dlume.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{name}.png
 
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Office;ContactManagement;
Name=Dlume
Comment=%{Summary}
EOF

%post 
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

