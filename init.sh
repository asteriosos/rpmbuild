#!/bin/bash

FOLDER1="/home/$USER/rpmbuild"
FILE1="/home/$USER/.rpmmacros"

if [ ! -d "$FOLDER1" ]; then
  echo "$FOLDER1 does not exists...creating it."
  mkdir $FOLDER1
  echo "Creating subdirs..."
  for i in BUILD RPMS SOURCES SPECS SRPMS tmp;do mkdir -p $FOLDER1/${i} && echo "$FOLDER1/${i}";done
else
  echo "$FOLDER1 exists."
fi

if [ ! -f "$FILE1" ]; then
echo "$FILE1 does not exists...creating it."
(
cat <<- EOF
%_topdir      $FOLDER1
%_tmppath     $FOLDER1/tmp
EOF
) > $FILE1
else
  echo "$FILE1 exists."
fi

if [ ! -f "$FOLDER1/SPECS/default.spec" ]; then
  echo "Copy default.spec to $FOLDER1/SPECS"
  cp default.spec $FOLDER1/SPECS/
  echo "Copied the default.spec to $FOLDER1/SPECS. Change the name of the spec file to your needs."
fi

if [ ! -f "/home/$USER/bin/buildrpm" ]; then
  echo "Copy buildrpm to ~/bin"
  cp buildrpm /home/$USER/bin/
  echo "Copied buidrom to your users bin folder. Run it with argument <name of your spec file> to build."
fi

echo "Copy the files that should be in the rpm to $FOLDER1/SOURCES"

