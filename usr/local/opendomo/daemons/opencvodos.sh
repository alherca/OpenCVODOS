#!/bin/sh
### BEGIN INIT INFO
# Provides:          opencvodos
# Required-Start:    
# Required-Stop:
# Should-Start:      
# Default-Start:     1 2 3 4 5
# Default-Stop:      0 6
# Short-Description: Vision
# Description:       Vision
#
### END INIT INFO

# Copyright(c) 2014 OpenDomo Services SL. Licensed under GPL v3 or later
DESC="OpenCVODOS"
PIDFILE="/var/opendomo/run/opencvodos.pid"
REFRESH="2"
CONFIGDIR="/etc/opendomo/vision/filters"
FILTERSDIR="/usr/local/opendomo/filters"

do_daemon() {
  	
  echo 1 > $PIDFILE
	
	cd $CONFIGDIR
	while test -f $PIDFILE
	do
		for i in *.conf
		do
			# All camerras
			ID=`basename $i | cut -f1 -d.`
			source ./$i
			# For all the cameras, apply filters
			cd $FILTERSDIR/$ID/
				for f in *.conf
				do
				IDF=`basename $f | cut -f1 -d.`
				source ./$f
				$FILTERSDIR/$IDF/$IDF.py $ID
				done
		done
		sleep $REFRESH
	done
}

do_start() {
	$0 daemon &
}
do_stop() {
	rm $PIDFILE
}

case "$1" in
	daemon)
		do_daemon
	;;

	start)
        log_daemon_msg "Starting $DESC" "$NAME"
        do_start
        log_end_msg 0
    ;;
	stop)
        log_daemon_msg "Stopping $DESC" "$NAME"
        do_stop
        log_end_msg 0
    ;;
	status)
        test -f $PIDFILE && exit 0 || exit $?
    ;;
	reload|force-reload|restart|force-reload)
        do_stop
		do_start
    ;;
	*)
        echo "Usage: $0 {start|stop|status|restart|force-reload}"
        exit 3
    ;;
esac
