# tracemap
Traceroute implementation in python with visualization on the worldmap with the leaflet JS library.

Usage: 
1. Run ```python3 main.py example.com``` ( sudo maybe needed on UNIX based Operating Systems. macOS doesn't allow creating RAW sockets without priviliges. One quick fix is to use a regular old UDP socket: Change ```receivingSock = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)``` to ```receivingSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, proto_icmp)``` )
3. Run the webpage at port number 5500; Or any other port if needed and make sure to edit the line 
  ```self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:xxxx')``` 
  by replacing xxxx with your port number in main.py
3. If the page is empty, refresh it after the main.py program echoes 'Server Started'

Note: If you only want the traceroute functionality, run ```python3 tracenot.py example.com```
  
<img width="526" alt="Screenshot 2023-06-06 at 3 41 44 PM" src="https://github.com/zaki-1337/tracemap/assets/107113588/ed2e9a00-14ef-458d-a8ce-57e7e0a00d0e">

<img width="1401" alt="Screenshot 2023-06-06 at 3 39 08 PM" src="https://github.com/zaki-1337/tracemap/assets/107113588/d35cb39d-0025-418a-bd0d-3f2734b7877a">
