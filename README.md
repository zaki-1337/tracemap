# tracemap
Traceroute implementation in python with visualization on the worldmap with the leaflet JS library.

Usage: 
1. Run ```python3 main.py example.com```
2. Run the webpage at port number 5500; Or any other port if needed and make sure to edit the line 
  ```self.send_header('Access-Control-Allow-Origin', 'http://127.0.0.1:xxxx')``` 
  by replacing xxxx with your port number in main.py
3. If the page is empty, refresh it after the main.py program echoes 'Server Started'

Note: If you only want the traceroute functionality, run ```python3 tracenot.py example.com```
  
<img width="423" alt="Screenshot 2023-06-06 at 3 26 00 PM" src="https://github.com/zaki-1337/tracemap/assets/107113588/6f62eb77-e346-42e0-a998-16d56dd2f1b2">

<img width="1401" alt="Screenshot 2023-06-06 at 3 39 08 PM" src="https://github.com/zaki-1337/tracemap/assets/107113588/d35cb39d-0025-418a-bd0d-3f2734b7877a">
