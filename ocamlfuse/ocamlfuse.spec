#
# spec file for package ocamlfuse
#
# Copyright (c) 2016-2022 Sérgio M. Basto.
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           ocamlfuse
Version:        2.7.1_cvs9
Release:        1%{?dist}
Summary:        Ocaml FUSE binding
License:        GPLv2
Url:            https://github.com/astrada/ocamlfuse/
Source:         https://github.com/astrada/ocamlfuse/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  fuse-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-runtime
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-dune-devel
BuildRequires:  ocaml-bigarray-compat-devel

%description
This is a binding to fuse for the ocaml programming language, enabling
you to write multithreaded filesystems in the ocaml language. It has
been designed with simplicity as a goal, as you can see by looking at
example/fusexmp.ml. Efficiency has also been a separate goal. The
Bigarray library is used for read and writes, allowing the library to
do zero-copy in ocaml land.

%prep
%autosetup -p1

%build
#Disable warnings to avoid spurious message about 64 bit compatibility
#due to a missing cast in a macro
#export CFLAGS="%{optflags} -w"
dune build @install

%install
dune install --destdir=%{buildroot} --prefix=/usr \
    --libdir=%{_libdir}/ocaml --docdir=%{_docdir}

%files
%doc %{_docdir}/ocamlfuse/README.md
%doc %{_docdir}/conf-libfuse/README.md
%license %{_docdir}/ocamlfuse/LICENSE
%license %{_docdir}/conf-libfuse/LICENSE
%{_libdir}/ocaml/conf-libfuse/
%{_libdir}/ocaml/ocamlfuse/
%{_libdir}/ocaml/stublibs/

%changelog
* Wed Feb 21 2024 Sérgio Basto <sergio@serjux.com> - 2.7.1_cvs9-1
- Update ocamlfuse to 2.7.1_cvs9

* Mon Dec 26 2022 Sérgio Basto <sergio@serjux.com> - 2.7.1_cvs7-3.20220109
- use --destdir=%%{buildroot}

* Sun Dec 25 2022 Sérgio Basto <sergio@serjux.com> - 2.7.1_cvs7-2.20220109
- Update to commits on Jan 9, 2022

* Thu Sep 09 2021 Sérgio Basto <sergio@serjux.com> - 2.7.1_cvs7-1
- New package versioning for ocamlfuse-2.7.1_cvs7
- Add the last 4 patches from git master

* Wed Sep 08 2021 Sérgio Basto <sergio@serjux.com> - 2.7.1-8.cvs7
- Update ocamlfuse to 2.7.1-cvs7

* Sun Nov 17 2019 Sérgio Basto <sergio@serjux.com> - 2.7.1-7.cvs6
- Update ocamlfuse to 2.7.1-cvs6

* Mon Jan 28 2019 Sérgio Basto <sergio@serjux.com> - 2.7.1-6.cvs5
- Add BR ocaml-runtime

* Thu Jan 25 2018 Sérgio Basto <sergio@serjux.com> - 2.7.1-5.cvs5
- Refresh ocamlfuse

* Thu Nov 02 2017 Sérgio Basto <sergio@serjux.com> - 2.7.1-4.cvs5
- Fix CFLAGS to not generate debug packages empty.

* Tue Jul 11 2017 Sérgio Basto <sergio@serjux.com> - 2.7.1-3.cvs5
- Update to 2.7.1-cvs5

* Tue Dec 06 2016 Sérgio Basto <sergio@serjux.com> - 2.7.1-2.cvs4
- Update to 2.7.1-cvs4

* Thu Mar 10 2016 Sérgio Basto <sergio@serjux.com> - 2.7.1-1.cv2
- Migrate to Fedora/Redhat.

* Sat Nov  7 2015 hpj@urpla.net
- version 2.7.1-cvs2: initial build
