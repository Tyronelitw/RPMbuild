#!/bin/bash
## my own rsync-based snapshot-style backup procedure
## (cc) Tangwei Li AT litangw@chinatelecom.cn

# config vars

SRC="rsync://mirrors.tuna.tsinghua.edu.cn/ceph/rpm-luminous/el7/x86_64/" #dont forget trailing slash!
DST="/data/repo/yum"
OPTS="-avrltgoi  --delete --no-iconv"
LOG="/data/repo/yum/rsync_status/ceph/ceph/"
MINCHANGES=32

# run this process with real low priority

ionice -c 3 -p $$
renice +12  -p $$

# sync

rsync $OPTS $SRC $DST/ctyun/rpm-luminous/el7/x86_64 > $DST/rsync_ceph.log

# check if enough has changed and if so
# make a hardlinked copy named as the date

COUNT=$( wc -l $DST/rsync_ceph.log|cut -d" " -f1 )
if [ $COUNT -gt $MINCHANGES ] ; then
DATETAG=$(date +%Y-%m-%d)
        if [ ! -e $LOG$DATETAG ] ; then
                mkdir $LOG$DATETAG
                mv $DST/rsync_ceph.log $LOG$DATETAG
        fi
fi
