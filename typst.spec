Name:       typst
Version:    0.14.2
Release:    1
Summary:    A new markup-based typesetting system that is powerful and easy to learn.

License:    Apache-2.0
URL:        https://github.com/typst/typst
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: cargo-rpm-macros >= 24
BuildRequires: openssl 
BuildRequires: openssl-libs
BuildRequires: openssl-devel
BuildRequires: perl
BuildRequires: perl-FindBin
BuildRequires: pkg-config
BuildRequires: rust-packaging >= 21

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

%prep
%autosetup

%build
# https://github.com/typst/typst/blob/main/crates/typst-cli/build.rs
export GEN_ARTIFACTS="artifacts"
cargo build -j${RPM_BUILD_NCPUS} -p typst-cli --release --all-features --locked


%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 target/release/typst %{buildroot}%{_bindir}/%{name}

# Artifacts 
export ARTIFACTS_DIR="crates/typst-cli/artifacts"
install -Dpm 0644 $ARTIFACTS_DIR/%{name}{,-compile,-fonts,-init,-query,-update,-watch}.1 -t %{buildroot}%{_mandir}/man1/
install -Dpm 0644 $ARTIFACTS_DIR/%{name}.bash -t %{buildroot}%{bash_completions_dir}
install -Dpm 0644 $ARTIFACTS_DIR/_%{name}     -t %{buildroot}%{zsh_completions_dir}
install -Dpm 0644 $ARTIFACTS_DIR/%{name}.fish -t %{buildroot}%{fish_completions_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

# Artifacts
%{_mandir}/*/*
%{bash_completions_dir}/%{name}.bash
%{zsh_completions_dir}/_%{name}
%{fish_completions_dir}/%{name}.fish

%changelog
%autochangelog
