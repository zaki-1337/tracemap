import datetime
import socket
import sys

def traceroute(hostname_or_address):
    ipList = []
    max_hops=30
    timeout=2
    destAddr = socket.gethostbyname(hostname_or_address)
    proto_icmp = socket.getprotobyname("icmp")
    # proto_udp = socket.getprotobyname("udp")
    port = 33434
    
    print('\nTracing Route to {0}\n'.format(hostname_or_address))

    for ttl in range(1, max_hops + 1):
        
        receivingSock = socket.socket(socket.AF_INET, socket.SOCK_RAW, proto_icmp)
        receivingSock.settimeout(timeout)
        receivingSock.bind(("", port))
        
        sendingSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sendingSock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        start = datetime.datetime.now()
        sendingSock.sendto("".encode(), (destAddr, port))

        try:
            _, currAddr = receivingSock.recvfrom(512)
            currAddr = currAddr[0]
        except socket.error:
            currAddr = "***.***.***.***"
        finally:
            end = datetime.datetime.now()
            receivingSock.close()
            sendingSock.close()

        print('Hop: {0} Address: {1} Delay: {2}ms'.format(str(ttl).rjust(2), currAddr.center(15), (end-start).microseconds/1000))
        
        if currAddr!="***.***.***.***":
            ipList.append(currAddr)

        if currAddr == destAddr:
            break
        
    return ipList

if __name__ == "__main__":
    dest_name = sys.argv[1]
    print(f"traceroute to {dest_name}")
    print(traceroute(dest_name))