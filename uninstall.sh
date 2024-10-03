#!/bin/bash
PWD=$(pwd)
NAME=live-server
COMMAND=/bin/$NAME
FILE_LIVE_SERVER=$PWD/live-server/$COMMAND.py
[ -f "$COMMAND" ] && rm -rf "$COMMAND"
[ -f "$FILE_LIVE_SERVER" ] && rm -rf "$FILE_LIVE_SERVER"