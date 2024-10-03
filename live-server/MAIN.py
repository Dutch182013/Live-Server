#!/usr/bin/env python

from os import environ
from HTTP_SERVER import init_server

init_server(environ["PWD"])