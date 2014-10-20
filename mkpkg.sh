#!/bin/sh
PKGID="opencvodos"
tar cvfz $PKGID-`date '+%Y%m%d'`.tar.gz --exclude .svn var
