Name:           rmpc-git
Version:        git
Release:        %autorelease
Summary:        Modern and configurable terminal Music Player Daemon client

License:        BSD-3-Clause
URL:            https://github.com/mierak/rmpc
Source0:        %{url}/archive/refs/heads/master.tar.gz

BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gcc
BuildRequires:  rust
BuildRequires:  rust-packaging
Recommends:     mpd

%description
rmpc is a modern terminal client for Music Player Daemon (MPD), focused on
speed, keyboard-driven workflows, and extensive configuration.

%generate_buildrequires
%cargo_generate_buildrequires

%prep
%autosetup -n rmpc-master
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/rmpc

%changelog
%autochangelog
