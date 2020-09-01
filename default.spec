#
# spec file for package default
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           default
Version:        1.0
Release:        0
Summary:        default
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL3
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          default 
Url:            default
Source:         %{name}.tar.gz 
#BuildRequires:  
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep

%setup -n %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/home/<user>/bin

install -m 700 ~/rpmbuild/SOURCES/%{name}/<filename> $RPM_BUILD_ROOT/home/<user>/bin/
%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

%files
%defattr(-,<user>,<user>)
/home/<user>/bin/<filename>

%changelog
* Tue Sep 01 2020  Your name here
- 1.0 r1 First release
