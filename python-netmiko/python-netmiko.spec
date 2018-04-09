%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global dist %(/usr/lib/rpm/redhat/dist.sh)
%global srcname netmiko
%global sum Multi-vendor library to simplify Paramiko SSH connections to network devices

Name:           python-netmiko
Version:        2.0.1
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
CTyun Cloud OpenStack Ironic Project networking-generic-switch Packages dependency package 
%{sum}


%package -n python2-%{srcname}
Summary:        %{sum}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-paramiko >= 1.13.0
Requires:       python2-scp >= 0.10.0
Requires:       PyYAML
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{sum} - package for Python 2.


%if 0%{?with_python3}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-paramiko >= 1.13.0
Requires:       python3-scp >= 0.10.0
Requires:       python3-PyYAML
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum} - package for Python 3.

%endif

# FIXME: build the documentation, when upstream starts shipping its sources:
# https://github.com/ktbyers/netmiko/issues/507


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%check
# FIXME: run unit tests, when upstream starts shipping them:
# https://github.com/ktbyers/netmiko/issues/508


%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%if 0%{?with_python3}

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%endif


%changelog
* Fri Jan 26 2018 Tangwei Li <litangw@chinatelecom.cn> - 2.0.1-1
- Initial for CTyun and update version to 2.0.1
* Mon Jun 26 2017 Dmitry Tantsur <divius.inside@gmail.com> - 1.4.1-1
- Initial packaging
