import socket
hostname="khyaathipython"
port=9910
try:
	s=socket.socket()
	s.connect((hostname,port))
	ack = s.recv(1024)
	print ack
	number=raw_input("enter a number:")
	s.send(number)
	resp_service = s.recv(1024)
	print resp_service
except Exception as err:
	print err
finally:
	s.close()

