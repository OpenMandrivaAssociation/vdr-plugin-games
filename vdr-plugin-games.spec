
%define plugin	games
%define name	vdr-plugin-%plugin
%define version	0.6.3
%define rel	10

Summary:	VDR plugin: OSD Games Collection
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://1541.org/
Source:		http://1541.org/public/vdr-%plugin-%version.tar.bz2
Patch0:		vdr-games-0.6.2-finnish.diff
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This is the new vdr OSD games collection formaly known as the tetris plugin.
The collection currently contains Tetris, Tron, TicTacToe, Snake and
Minesweeper, more to come.

%prep
%setup -q -n %plugin-%version
%patch0 -p1 -b .fi

%build
%vdr_plugin_build libvdr-games.so CFLAGS="%{optflags} -fPIC -I%{_includedir}/vdr" -j1

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README TODO COPYING HISTORY


