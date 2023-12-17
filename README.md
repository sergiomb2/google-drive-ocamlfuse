# google-drive-ocamlfuse
Packaging google-drive-ocamlfuse
Builds available here: https://copr.fedorainfracloud.org/coprs/sergiomb/google-drive-ocamlfuse/

1 - Prepare ocamlfuse
```
   cd ocamlfuse
   spectool -g ocamlfuse.spec
   rpmbuild -bs ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
   # optional
   mock -r fedora-23-x86_64 --no-clean --rebuild ./ocamlfuse-2.7.1-1.cv2.fc23.src.rpm
   or
   copr-cli build sergiomb/google-drive-ocamlfuse ./ocamlfuse-2.7.1-2.cvs4.fc23.src.rpm
   or
   fedpkg --release rawhide copr-build sergiomb/google-drive-ocamlfuse
   cd ..
```

2 - Prepare gapi-ocaml
```
    cd gapi-ocaml
    rpmdev-bumpspec -n 0.3.6 -c "Update gapi-ocaml to 0.3.6" gapi-ocaml.spec
    spectool -g gapi-ocaml.spec
    rpmbuild -bs gapi-ocaml.spec --define "_sourcedir ." --define "_srcrpmdir ."
    # optional
    mock -r fedora-23-x86_64 --no-clean --rebuild ./gapi-ocaml-0.2.10-1.fc23.src.rpm
    or
    copr-cli build sergiomb/google-drive-ocamlfuse ./gapi-ocaml-0.3.1-1.fc23.src.rpm
    cd ..
```

3 - Prepare google-drive-ocamlfuse
```
    cd google-drive-ocamlfuse/
    rpmdev-bumpspec -n 0.6.20 -c "Update google-drive-ocamlfuse to 0.6.20" google-drive-ocamlfuse.spec
    spectool -g google-drive-ocamlfuse.spec
    rpmbuild -bs google-drive-ocamlfuse.spec --define "_sourcedir ." --define "_srcrpmdir ."
    cd ..
```

4 - Build google-drive-ocamlfuse in chain
```
    mockchain -r fedora-23-x86_64 -l resultsdir \
    ocamlfuse/ocamlfuse-2.7.1-1.cv2.fc23.src.rpm \
    gapi-ocaml/gapi-ocaml-0.2.10-1.fc23.src.rpm \
    google-drive-ocamlfuse/google-drive-ocamlfuse-0.5.22-2.fc23.src.rpm
```

and the rpm is in resultsdir/results/fedora-23-x86_64/google-drive-ocamlfuse-0.5.22-2.fc23/
