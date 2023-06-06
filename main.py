import socket
import sys
from locator import *
from tracenot import traceroute
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# get hostname from parse
if len(sys.argv)<2:
    print('''Usage:
        python main.py [hostname]
    
    Example:
        python main.py google.com
    
    ''')
    exit()
    
hostname = sys.argv[1]

# get my location (myIP,(lon,lat),city)
myLoc = getMyLoc()

# get target location IP,(lon,lat),city
targetIP = socket.gethostbyname(hostname)
targetLoc = getTargetLoc(targetIP)

# traceroute process to hostname and output the ipList : (ipAddress,(lon,lat),city)
ipList = traceroute(targetIP)

# get geo location of the ipList and insert myLoc and TargetLoc
routeLocList = getLoc(ipList)
routeLocList.insert(0,myLoc)
routeLocList.append(targetLoc)

# prepare for and linear route in map
responseList = []
tempLon = 0
tempLat = 0
for x in routeLocList:
    # this looping will drop the route that have zero movement
    if x[1][0]-tempLon == 0 or x[1][1]-tempLat == 0:
        continue
    responseList.append(x)

    tempLon = x[1][0]
    tempLat = x[1][1]

# send data to JS
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.end_headers()
        response = {'routeArray': responseList}
        self.wfile.write(json.dumps(response).encode())


server_address = ('', 8002)
httpd = HTTPServer(server_address, MyServer)
print('\nServer Started.')
httpd.serve_forever()