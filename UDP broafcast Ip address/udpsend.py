import socket
UDP_IP = "192.168.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.connect(("8.8.8.8", 80))
print(sock.getsockname())
#MESSAGE = b"Hello, World!"
ipaddress=sock.getsockname()[0].encode()
hostname=socket.gethostname().encode()
#MESSAGE=s.getsockname()[0].encode()
#print("message: %s" % MESSAGE)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
for i in range (1,254):
#    print("UDP target IP: %s" % UDP_IP)
#    print("UDP target port: %s" % UDP_PORT)
    UDP_IP = "192.168.0."+str(i)
#    print (UDP_IP)
    sock.sendto(ipaddress, (UDP_IP, UDP_PORT))
    sock.sendto(hostname, (UDP_IP, UDP_PORT))
