#
# spec file for package ocaml-tiny_httpd
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ocaml-tiny_httpd
Version:        0.11
Release:        1%{?dist}
%{?ocaml_preserve_bytecode}
Summary:        Minimal HTTP server using good old threads
License:        MIT
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/tiny_httpd
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-zip

%description
Minimal HTTP server using good old threads.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune build @install

%install
dune install --destdir=%{buildroot} --prefix=/usr \
    --libdir=%{_libdir}/ocaml --docdir=%{_docdir}


%files
%{_bindir}/*
%doc %{_docdir}/tiny_httpd_camlzip/README.md
%doc %{_docdir}/tiny_httpd_camlzip/CHANGES.md
%doc %{_docdir}/tiny_httpd/README.md
%doc %{_docdir}/tiny_httpd/CHANGES.md
#%%license %%{_docdir}/tiny_httpd_camlzip/LICENSE
#%%license %%{_docdir}/conf-libfuse/LICENSE
%{_libdir}/ocaml/tiny_httpd/
%{_libdir}/ocaml/tiny_httpd_camlzip/
%exclude %{_libdir}/ocaml/tiny_httpd/*.a
%exclude %{_libdir}/ocaml/tiny_httpd/*.cmx
%exclude %{_libdir}/ocaml/tiny_httpd/*.cmxa
%exclude %{_libdir}/ocaml/tiny_httpd/*.mli
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.a
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.cmx
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.cmxa
%exclude %{_libdir}/ocaml/tiny_httpd_camlzip/*.mli


%files devel
%{_libdir}/ocaml/tiny_httpd/*.a
%{_libdir}/ocaml/tiny_httpd/*.cmx
%{_libdir}/ocaml/tiny_httpd/*.cmxa
%{_libdir}/ocaml/tiny_httpd/*.mli
%{_libdir}/ocaml/tiny_httpd_camlzip/*.a
%{_libdir}/ocaml/tiny_httpd_camlzip/*.cmx
%{_libdir}/ocaml/tiny_httpd_camlzip/*.cmxa
%{_libdir}/ocaml/tiny_httpd_camlzip/*.mli

%changelog
