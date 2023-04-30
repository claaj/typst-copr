Name:       typst
Version:    0.3.0
Release:    1%{dist}
Summary:    A new markup-based typesetting system that is powerful and easy to learn.

License:    Apache-2.0
URL:        https://github.com/typst/typst
%undefine _disable_source_fetch
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

ExclusiveArch: %{rust_arches}

BuildRequires: cargo
BuildRequires: rust

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

%global debug_package %{nil}

%prep
%autosetup

%build
cargo build -p typst-cli --release --all-features

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog