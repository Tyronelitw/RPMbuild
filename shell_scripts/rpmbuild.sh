#/bin/bash
spec=$1
sourcesdir=/root/rpmbuild/SOURCES/
rpmdir=/root/rpmbuild/RPMS/noarch/
specdir=/root/rpmbuild/SPECS/
# get project name
if [[ "${spec}" =~ 'python' ]]; then
         project=${spec}
    else
         project=$(echo ${spec} | cut -d "-" -f 2)
    fi


# get version number
old_rpm=$(find ${rpmdir} | grep "${spec}" | sort -V | tail -1 )
version=$(rpm -qp --qf  "%{VERSION}" "${old_rpm}")

# get source_code_tarball
source_code_dir=${project}
source_code_tarball="${source_code_dir}-${version}.tar.gz"

# get package source code 
cd ${sourcesdir}
        if [ -d ${source_code_dir} ]; then
          rm -rf ${source_code_dir}
        fi

git clone ssh://jenkins@172.18.211.200:29418/pike/${project} && cd ${source_code_dir}
python setup.py sdist --quiet > /dev/null
mv -f "${sourcesdir}/${source_code_dir}/dist/${source_code_tarball}" "${sourcesdir}"
cd ${specdir}

# get  release number
old_release=$(rpm -qp --qf  "%{RELEASE}" "${old_rpm}" | awk -F'.' '{print $1}')

# write version and release number to spec file
new_release=$(expr "${old_release}" + 1)
#sed -i "s/Version:\([ \t]*\).*$/Version:\1${version}/g" openstack-cinder.spec
sed -i "s/Release:\([ \t]*\)\([0-9]*\)\(.*$\)/Release:\1${new_release}\3/g" ${spec}.spec

# build package
rpmbuild -ba ${spec}.spec
# sync package  
rsync -avz ${rpmdir} root@172.28.8.221:/data/repo/yum/ctyun/centos/7/cloud/x86_64/openstack-pike/
