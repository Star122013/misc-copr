Name:           rmpc-git
Version:        git
Release:        %autorelease
Summary:        Modern and configurable terminal Music Player Daemon client

License:        BSD-3-Clause
URL:            https://github.com/mierak/rmpc
Source0:        %{url}/archive/refs/heads/master.tar.gz

BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  rust
Recommends:     mpd

%description
rmpc is a modern terminal client for Music Player Daemon (MPD), focused on
speed, keyboard-driven workflows, and extensive configuration.

%prep
%autosetup -n rmpc-master

%build
export CARGO_HOME=%{_builddir}/.cargo
export RUSTFLAGS="%{build_rustflags}"
cargo build --release --locked --bins

%install
install -Dpm0755 target/release/rmpc %{buildroot}%{_bindir}/rmpc

%files
%license LICENSE
%doc README.md
%{_bindir}/rmpc

%changelog
%autochangelog
