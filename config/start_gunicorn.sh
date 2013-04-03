#!/bin/bash
set -e
LOGFILE=/tmp/guni.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3  # cpu core nums * 2 + 1
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS \
  --daemon \
  --log-level=error \
  --log-file=$LOGFILE 2>>$LOGFILE \
  hilton_trade.wsgi:application