from socket import *

port = 6464
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))
s.listen(5)
conn, addr = s.accept()
print "Connected to server - ", addr

while 1:
	data = conn.recv(1024)
	print "Received ", repr(data)

conn.close()