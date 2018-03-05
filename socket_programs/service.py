# hostname, port
# make url: bind(host,port)
# wait for the clcinet request
# if the client sends a request then acdept
# process the request
# send the respponse

import socket
hostname=socket.gethostname()
port = 9910
try:
	s=socket.socket()
	s.bind((hostname,port))
	while True:
		s.listen(6)
		print "waiting for the client request."
		print "Running: %s:%s"%(hostname,port)
		#print s.accept()
		co,ci=s.accept()
		co.send("Hello firefox .. How are you doing")
		req_data = co.recv(1024)
		resp = "EVEN" if int(req_data)%2==0 else "ODD"
		co.send(resp)
except Exception as err:
	print err
finally:
	s.close()