#!/bin/bash
PWD=$(pwd)
NAME=live-server
COMMAND=/bin/$NAME
FILE_LIVE_SERVER=$PWD/$NAME$COMMAND.py
FILE_DEFAULT=$PWD/$NAME/MAIN.py
if [ -f "$COMMAND" ]; then
    echo "$NAME: installing."
else
    echo "install-command: $NAME"
    if [ -f "$FILE_LIVE_SERVER" ]; then
        ln -s "$FILE_LIVE_SERVER" "$COMMAND"
        echo "$COMMAND installing."
    else
        if [ -f "$FILE_DEFAULT" ]; then
            ln -s "$FILE_DEFAULT" "$FILE_LIVE_SERVER"
            echo "$FILE_LIVE_SERVER installing."
            ln -s "$FILE_LIVE_SERVER" "$COMMAND"
            echo "$COMMAND installing."
        else
            echo " $FILE_DEFAULT errs. : test reinstall"
        fi
    fi
fi
