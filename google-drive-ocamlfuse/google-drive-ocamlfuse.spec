#
# spec file for package google-drive-ocamlfuse
#
# Copyright (c) 2016 Sérgio Basto.
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:       google-drive-ocamlfuse
Version:    0.7.31
Release:    1%{?dist}
License:    BSD-2-Clause
Summary:    FUSE filesystem for Google Drive
Url:        http://gdfuse.forge.ocamlcore.org
Source:     https://github.com/astrada/google-drive-ocamlfuse/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml >= 3.12.0
BuildRequires:  ocaml-findlib-devel >= 1.2.7
BuildRequires:  ocamlfuse >= 2.7.1
BuildRequires:  gapi-ocaml-devel >= 0.2.10
BuildRequires:  ocaml-sqlite-devel >= 1.6.1
BuildRequires:  ocaml-cryptokit-devel
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-yojson-devel
BuildRequires:  ocaml-biniou-devel
BuildRequires:  ocaml-easy-format-devel
BuildRequires:  ocaml-curl-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-tiny_httpd-devel
BuildRequires:  sqlite-devel
BuildRequires:  curl-devel
BuildRequires:  zlib-devel
BuildRequires:  fuse-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-seq-devel


%description
google-drive-ocamlfuse is a FUSE-based file system backed by Google Drive,
written in OCaml. It lets you mount your Google Drive on Linux.

On the first time, just run google-drive-ocamlfuse, which will open a
browser for authentication. If that process succeeds, it will print
"Access token retrieved correctly.". Now run google-drive-ocamlfuse
with an empty directory supplied, which is the mount point for your Google
Drive. You can optionally unmount with fusermount -u mount-point.

Further documentation is available here:

  https://github.com/astrada/google-drive-ocamlfuse/wiki


%prep
%setup -q

%build
dune build @install

%install
dune install --destdir=%{buildroot} --prefix=/usr --libdir=%{_libdir}/ocaml --docdir=%{_docdir}


%files
%doc doc/
%doc %{_docdir}/%{name}/README.md
%license %{_docdir}/%{name}/LICENSE
%{_bindir}/%{name}
%{_libdir}/ocaml/%{name}


%changelog
* Thu Feb 22 2024 Sérgio Basto <sergio@serjux.com> - 0.7.31-1
- Update google-drive-ocamlfuse to 0.7.31

* Fri Dec 30 2022 Sérgio Basto <sergio@serjux.com> - 0.7.30-1
- message

* Wed Nov 03 2021 Sérgio Basto <sergio@serjux.com> - 0.7.27-1
- Update google-drive-ocamlfuse to 0.7.27

* Wed Sep 08 2021 Sérgio Basto <sergio@serjux.com> - 0.7.26-1
- Update google-drive-ocamlfuse to 0.7.26

* Tue Nov 19 2019 Sérgio Basto <sergio@serjux.com> - 0.7.14-1
- Update google-drive-ocamlfuse to 0.7.14

* Mon Jan 28 2019 Sérgio Basto <sergio@serjux.com> - 0.7.1-1
- Update google-drive-ocamlfuse to 0.7.1

* Thu Jan 25 2018 Sérgio Basto <sergio@serjux.com> - 0.6.24-1
- Update google-drive-ocamlfuse to 0.6.24

* Sun Nov 05 2017 Sérgio Basto <sergio@serjux.com> - 0.6.21-1
- Update google-drive-ocamlfuse to 0.6.21
- Enable debuginfo

* Sat Jul 22 2017 Sérgio Basto <sergio@serjux.com> - 0.6.20-1
- Update google-drive-ocamlfuse to 0.6.20

* Tue Jul 11 2017 Sérgio Basto <sergio@serjux.com> - 0.6.17-1
- Update to 0.6.17

* Tue Dec 06 2016 Sérgio Basto <sergio@serjux.com> - 0.6.2-1
- Update to 0.6.2

* Fri Apr 22 2016 Sérgio Basto <sergio@serjux.com> - 0.5.22-2
- Rebuild for gapi-ocaml-0.2.10

* Thu Mar 10 2016 Sérgio Basto <sergio@serjux.com> - 0.5.22-1
- Update to 0.5.22

* Mon Sep 28 2015 hpj@urpla.net
- update to version 0.5.18 (no changelog available)
* Sun Mar 29 2015 hpj@urpla.net
- update to version 0.5.13 (no changelog available)
* Tue Jan  6 2015 hpj@urpla.net
- version 0.5.12: initial build
