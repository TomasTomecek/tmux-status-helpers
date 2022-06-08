%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         TomasTomecek
%global repo            tmux-top
# https://github.com/TomasTomecek/tmux-top
%global goipath         %{provider}.%{provider_tld}/%{project}/%{repo}
%global forgeurl        https://%{goipath}
# %%global commit          910ef1f72549a703c3c39abaefefe9a80d0b22fd
%global golicenses      LICENSE
%global godocs          README.md
# since tmux-top release archives are structured as NAME-VERSION
# 1. We need to set version
# 2. And cannot set commit macro
# 3. Place version before gometa
Version:        0.1.1
%gometa

Name:           tmux-top
Release:        1%{?dist}
Summary:        Monitoring information for your tmux status line.
License:        GPLv2+
URL:            %{gourl}
# gosource macro doesn't work as it expects vTAG tagging scheme
Source0:        https://%{goipath}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  golang(github.com/urfave/cli)


%description
Monitoring information for your tmux status line.

tmux-top allows you to see your:

 * load
 * memory usage
 * network information
 * I/O

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/tmux-top


%install
%gopkginstall
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/


%check
export GOPATH=$(pwd):%{gopath}
make test


%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/%{name}

%gopkgfiles


%changelog
* Wed Jun 08 2022 Tomas Tomecek <ttomecek@redhat.com> - 0.1.1-1
- 0.1.0 upstream release

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 29 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.0.4-1
- new upstream release 0.0.4

* Sun Oct 29 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.0.3-1
- new upstream release 0.0.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.0.2-1
- new upstream release 0.0.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-6
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-5
- https://fedoraproject.org/wiki/Changes/golang1.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Tomas Tomecek <ttomecek@redhat.com> - 0.0.1-2
- add devel subpackage (patch by jchaloup@redhat.com)

* Fri Mar 13 2015 Tomas Tomecek <ttomecek@redhat.com> - 0.0.1-1
- initial release

