#!/bin/sh
#desc:Configure OpenCVODOS
#package:opencvodos
#type:local

# Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later

DEVNAME="opencvodos"
CONFIGDIR="/etc/opendomo/vision/filters/"
CAMDIR="/etc/opendomo/control/"
CFGFILE="/etc/opendomo/$DEVNAME.conf"

test -d $CONFIGDIR || mkdir $CONFIGDIR

if test -f $CFGFILE;
then
	source $CFGFILE
fi
