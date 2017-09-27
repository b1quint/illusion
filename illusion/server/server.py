"""
#===========================================================================
# Illusion Server v0.1
#
# by Bruno Quint, 01.11.2010
#---------------------------------------------------------------------------
# A TCP/IP server that connects Illusion Engine to other interfaces by 
# receiving commands and translating them to a config file needed to run the 
# Engine.
#===========================================================================
#"""

import os
import subprocess
import socket
import sys
import time

print __doc__
execfile("./Conf/server_config.py")

myHost = SConfig.host
myPort = SConfig.port

######
## TIMESTAMP data no tipo AAAAMMDDHHmmss  20021017155933
timestamp = ( "%04i%02i%02i%02i%02i%02i" %     \
             ( int(`time.localtime()[0]`),  \
               int(`time.localtime()[1]`),  \
               int(`time.localtime()[2]`),  \
               int(`time.localtime()[3]`),  \
               int(`time.localtime()[4]`),  \
               int(`time.localtime()[5]`) ) )

print '# Loading server at ', myHost, ' port number ', myPort    
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
mySocket.bind((myHost, myPort))
mySocket.listen(1)
print '# Server loaded!'
print '# Now waiting for new connections'
    
while True:
    (conn, addr) = mySocket.accept()
    print '# Opening connection with', addr
    conf_name = "./Conf/obsconf_" + timestamp + ".py"
    file = open(conf_name, "wb")
    while True:
        data = conn.recv(1024)
        if not data: break
        file.write(data)
    print '# Transfer ended'
    print '# Closing connection with', addr
    file.close()
    conn.close()
    
    subprocess.Popen(["python","./Engine/engine.py",conf_name])
    
### END OF FILE ###
