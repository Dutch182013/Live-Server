#!/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from random import random as rand
from math import floor

def init_server(PATH = ""):
    if PATH != "":
        text_html = open(PATH + "/index.html").read()
        if text_html != "":
            class helloHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    self.path = PATH
                    try:
                        file_to_open = text_html
                        self.send_response(200)
                    except:
                        file_to_open = "file not found"
                        self.send_response(404)
                    self.send_header('content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(bytes(file_to_open, 'utf-8'))
            
            def setHost():
                readHost = open("/etc/hosts").read()
                hostsname = []
                host = ""
                number_host = 0
                for readstr in readHost:
                    if readstr == " " or readstr == "\n":
                        hostsname.append(host)
                        host = ""
                        number_host += 1
                    else:
                        host += str(readstr)
                return(hostsname[int(rand() * number_host)])
            
            HTTP_HOST = setHost()
            HTTP_PORT = 8000
            server = HTTPServer((HTTP_HOST, HTTP_PORT),helloHandler)
            print(' Server running on port http://' + HTTP_HOST + ":" + str(HTTP_PORT))
            server.serve_forever()
        else:
            print(" index.html not fonts ")
    else:
        print(" PATH not fonts ")