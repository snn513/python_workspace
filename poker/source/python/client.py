# client

import socket 
import sys

print 'Number of argument:',len(sys.argv),'argument.'
print 'Argument List', str(sys.argv)
print sys.argv[1] 
print int(sys.argv[2])

#address = ('127.0.0.1', 31500)
address = (sys.argv[1], int(sys.argv[2]))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(512)
print 'the data received is',data

s.send('hihi')

s.close()
