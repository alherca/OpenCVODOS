#!/bin/sh
#desc:Configure OpenCVODOS
#package:opencvodos
#type:local

# Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later

DEVNAME="opencvodos"
CFGFILE="/etc/opendomo/$DEVNAME.conf"

if test -f $CFGFILE;
then
	source $CFGFILE
fi
