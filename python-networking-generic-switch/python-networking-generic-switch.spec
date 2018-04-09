%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global srcname networking_generic_switch
%global pkgname networking-generic-switch
%global common_summary Pluggable Modular Layer 2 Neutron Mechanism driver
%global dist %(/usr/lib/rpm/redhat/dist.sh)

Name:           python-networking-generic-switch
Version:        0.5.1
Release:        5
Summary:        %{common_summary}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{pkgname}
Source0:        https://tarballs.openstack.org/%{pkgname}/%{pkgname}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git
BuildRequires:  openstack-macros
BuildRequires:  python2-devel
BuildRequires:  python-pbr
# for documentation
BuildRequires:  python-oslo-sphinx
BuildRequires:  python-sphinx
# for unit tests
BuildRequires:  /usr/bin/ostestr
BuildRequires:  python-mock
BuildRequires:  python-fixtures
BuildRequires:  python-netmiko
BuildRequires:  python-neutron-lib
BuildRequires:  python-neutron-tests
BuildRequires:  python-oslo-config
BuildRequires:  python-oslo-i18n
BuildRequires:  python-oslo-log
BuildRequires:  python-six
BuildRequires:  python-stevedore
BuildRequires:  python-tenacity
BuildRequires:  python-tooz

%description
CTyun Cloud OpenStack Ironic Project 
Pluggable Modular Layer 2 Neutron Mechanism driver implementing functionality
required for use-cases like OpenStack Ironic multi-tenancy mode.

%prep
%autosetup -n %{pkgname}-%{upstream_version} -S git
%py_req_cleanup

%build
%py2_build
%{__python2} setup.py build_sphinx -b html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
#ostestr --path %{srcname}/tests/unit

%install
%py2_install


%package -n python2-%{pkgname}
Summary:        %{common_summary}
%{?python_provide:%python_provide python2-%{pkgname}}

Requires:       python-netmiko >= 2.0.1
Requires:       python-neutron-lib >= 1.9.0
Requires:       python-oslo-config >= 5.1.0
Requires:       python-oslo-i18n >= 3.15.3
Requires:       python-oslo-log >= 3.30.0
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-tenacity >= 3.2.1
Requires:       python-tooz >= 1.58.0
Requires:       python-treelib >= 1.5.1
Requires:       python-textfsm >= 0.4.0
Requires:       pyserial >= 2.6.6

%description -n python2-%{pkgname}
Pluggable Modular Layer 2 Neutron Mechanism driver implementing functionality
required for use-cases like OpenStack Ironic multi-tenancy mode.

This package contains the plugin itself.


%package -n python2-%{pkgname}-tests
Summary:        %{common_summary} - tests

Requires:       python2-%{pkgname} = %{version}-%{release}
Requires:       python-mock >= 2.0.0
Requires:       python-neutron-tests
Requires:       python-fixtures >= 3.0.0

%description -n python2-%{pkgname}-tests
Pluggable Modular Layer 2 Neutron Mechanism driver implementing functionality
required for use-cases like OpenStack Ironic multi-tenancy mode.

This package contains the unit tests.


%package doc
Summary:        %{common_summary} - documentation

%description doc
Pluggable Modular Layer 2 Neutron Mechanism driver implementing functionality
required for use-cases like OpenStack Ironic multi-tenancy mode.

This package contains the documentation.


%files -n python2-%{pkgname}
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}*.egg-info
%exclude %{python2_sitelib}/%{srcname}/tests

%files -n python2-%{pkgname}-tests
%license LICENSE
%{python2_sitelib}/%{srcname}/tests

%files doc
%license LICENSE
%doc doc/build/html README.rst


%changelog
* Thu Mar 29 2018 Tangwei Li <litangw@chinatelecom.cn> - 0.5.1-5
- Modify Requires python-pyserial to pyserial.
* Tue Mar 27 2018 Tangwei Li <litangw@chinatelecom.cn> - 0.5.1-4
- Add Requires (textfsm/pyserial) and Update To Version 0.5.1-4 And Build Package.
* Mon Mar 26 2018 Tangwei Li <litangw@chinatelecom.cn> - 0.5.1-3
- Add Requires treelib and Update To Version 0.5.1-3 And Build Package.
* Fri Mar 23 2018 Tangwei Li <litangw@chinatelecom.cn> - 0.5.1-2
- Update To Version 0.5.1-2 And Build Package.
* Thu Jan 25 2018 Tangwei Li <litangw@chinatelecom.cn> - 0.5.1-1
- Initial And Update To Version 0.5.1 Add Requires netmiko to devlop branch for 2.0.1 And Build Package.
