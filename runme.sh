fuse_ver=2.7.1_cvs7
gapi_ver=0.4.2
googledrive_ver=0.7.30
fver=37

if [ -z "$1" ]
then
    stage=0
else
    stage=$1
fi

if test $stage -le 0
then
echo STAGE 0
cd ocamlfuse
rpmdev-bumpspec -n $fuse_ver -c "Update ocamlfuse to $fuse_ver" ocamlfuse.spec
spectool -g ocamlfuse.spec
fedpkg --release f37 srpm
# optional
#mock -r fedora-23-x86_64 --no-clean --rebuild ./ocamlfuse-2.7.1-1.cv2.fc23.src.rpm
#or
fedpkg --release f37 copr-build sergiomb/google-drive-ocamlfuse
cd ..
echo Press enter to continue to gapi-ocaml; read dummy;
fi
if test $stage -le 1
then
echo STAGE 1
cd gapi-ocaml
rpmdev-bumpspec -n $gapi_ver -c "Update gapi-ocaml to $gapi_ver" gapi-ocaml.spec
spectool -g gapi-ocaml.spec
# optional
#fedpkg --release f37 mockbuild -N
fedpkg --release f37 copr-build sergiomb/google-drive-ocamlfuse
cd ..
echo Press enter to continue to google-drive-ocamlfuse; read dummy;
fi
if test $stage -le 2
then
echo STAGE 2
cd google-drive-ocamlfuse/
rpmdev-bumpspec -n $googledrive_ver -c "Update google-drive-ocamlfuse to $googledrive_ver" google-drive-ocamlfuse.spec
spectool -g google-drive-ocamlfuse.spec
fedpkg --release f37 mockbuild -N -- -a https://download.copr.fedorainfracloud.org/results/sergiomb/google-drive-ocamlfuse/fedora-37-x86_64/
fedpkg --release f37 copr-build sergiomb/google-drive-ocamlfuse

cd ..
fi

#mockchain -r fedora-23-x86_64 -l resultsdir \
#ocamlfuse/ocamlfuse-2.7.1-1.cv2.fc23.src.rpm \
#gapi-ocaml/gapi-ocaml-0.2.10-1.fc23.src.rpm \
#google-drive-ocamlfuse/google-drive-ocamlfuse-0.5.22-2.fc23.src.rpm
#and the rpm is in resultsdir/results/fedora-23-x86_64/google-drive-ocamlfuse-0.5.22-2.fc23/
