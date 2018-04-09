%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global dist %(/usr/lib/rpm/redhat/dist.sh)
%global srcname treelib
%global sum Multi-vendor library to simplify Paramiko SSH connections to network devices

Name:           python-treelib
Version:        1.5.1
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
CTyun Cloud OpenStack Ironic Project networking-generic-switch Packages dependency package.

%package -n python2-%{srcname}
Summary:        %{sum}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
#Requires:      
#Requires:      
#Requires:      
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{sum} - package for Python 2.


%if 0%{?with_python3}

%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#Requires:
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{sum} - package for Python 3.

%endif

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

%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/*

%if 0%{?with_python3}

%files -n python3-%{srcname}
%license LICENSE
%doc README.md

%endif


%changelog
* Mon Mar 26 2018 Tangwei Li <litangw@chinatelecom.cn> - 1.5.1-1
- Initial and Build RPM package  version to 1.5.1
