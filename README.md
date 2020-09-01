# rpmbuild
rpmbuild stuff for suse systems

the package rpm-build should be installed
  - sudo zypper in rpm-build

install
  - git clone this repo
  - run ./init.sh
  - edit the spec file to your needs user & filename

after that you should generate a gpg for rpm signing and import it to rpm.
  - gpg --gen-key
  - gpg --list-keys
  - gpg --export -a 'your name' > RPM-GPG-KEY-<your_name>
  - sudo rpm --import RPM-GPG-KEY-<your_name>
  - rpm --addsign your.rpm
  - rpm --checksig your.rpm

