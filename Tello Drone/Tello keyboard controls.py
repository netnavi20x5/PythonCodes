#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
# refer https://dl-cdn.ryzerobotics.com/downloads/tello/20180910/Tello%20SDK%20Documentation%20EN_1.3.pdf
# 1/1/2018

#todo
#variant speed
#activate camera
#global varable angel
#global varable distance
#emergency stop


import threading 
import socket
import sys
import time

spd=10 #initilize drone speed
rotate=10 #initilize drone CCW and CW rotations 10-3600
distant=20 # initilize drone movement distance 20-500 
speed = 10 #initlize speed 10-100


import msvcrt
from msvcrt import getch


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

#Use Keytest.py to find the keyboard input 
def keyboard_input():
		key = ord(getch())
		global speed
		#print(key) #debugging
		if key == 27: #ESC
			print("end")
			return "end"
		elif key == 24: #Space
			print("emergency")
			return "emergency"
		elif key == 3: #Space
			print("speed 10")
			return "speed 10"
		elif key == 32: #Space
			print("command")
			return "command"
		elif key == 119: #w
			print("up "+str(distant))
			return "up "+str(distant)
		elif key == 115: #s
			print("down "+str(distant))
			return "down "+str(distant)
		elif key == 97: #a
			print("ccw "+str(rotate))
			return "ccw "+str(rotate)
		elif key == 100: #d
			print("cw "+str(rotate))
			return "cw "+str(rotate)
		elif key == 72: #up
			print("forward "+str(distant))
			return "forward "+str(distant)
		elif key == 80: #down
			print("back "+str(distant))
			return "back "+str(distant)
		elif key == 75: #left
			print("left "+str(distant))
			return "left "+str(distant)
		elif key == 77: #right
			print("right "+str(distant))
			return "right "+str(distant)
		elif key == 13: #takeoff
			print("takeoff")
			return "takeoff"
		elif key == 10: #takeoff
			print("land")
			return "land"
		elif key == 59: #takeoff
			print("streamon")
			return "streamon"
		elif key == 60: #takeoff
			print("streamoff")
			return "streamoff"
		elif key == 122: #z
			speed += 10
			if speed >=100:
				speed =100
			print("speed "+str(speed))
			return "speed "+str(speed)
		elif key == 120: #x
			speed -= 10
			if speed <=10:
				speed=10
			print("speed "+str(speed))
			return "speed "+str(speed)
		else:
			print("invalid key")
			return "a"


print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

while True: 

    try:
        #msg = input("");
        msg = keyboard_input();

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break




