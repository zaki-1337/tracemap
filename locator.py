import requests

def getMyLoc():
    url='http://ip-api.com/json/'
    response = requests.get(url)
    data = response.json()
    try:
        myIP = data['query']
        lon =data['lon']
        lat = data['lat']
        city = data['city']
    except KeyError as a:
        print(f'Error: {a} Not Found')
        exit()

    return (myIP,(lat,lon),city)

def getTargetLoc(IP):
    url = f'http://ip-api.com/json/{IP}?fields=16592'
    response = requests.get(url)
    data = response.json()
    try:
        lon =data['lon']
        lat = data['lat']
        city = data['city']
    except KeyError as a:
        print(f'Error: {a} Not Found')
        exit()

    return (IP,(lat,lon),city)



def getLoc(ipList):
    List = []
    for ipAddress in ipList:
        url = f'http://ip-api.com/json/{ipAddress}?fields=16592'
        response = requests.get(url)
        data = response.json()
        
        # check if IP is private ip
        try:
            if data['status'] != 'success':
                continue
        except KeyError:
            pass

        
        lon =data['lon']
        lat = data['lat']
        if lon == None or lat == None:
            continue
        city = data['city']
        List.append((ipAddress,(lat,lon),city))

    return List