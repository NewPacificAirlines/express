
#!/usr/bin/env python3
"""Send file to PECTAB based printer


Usage:

    send_BTP.py path address
    
"""


import sys
import re
import time
import socket
import subprocess


def send_Pectab_file(filename, ip_address):

    try:
        print(filename) 
        print(ip_address)
        
        host = ip_address           # target address
        port = '9090'                   # Reserve a port for your service.
        
        command = 'nc '+ host +' '+ port + ' < '+filename
        
        print(command)
        subprocess.Popen(command,shell=True)
        
        
        
    except:
        print('Error occured')  
    
  
        
        

if __name__ == '__main__':
       
    try:
        filename = sys.argv[1]      #The 0th arg is the module filename.
        ip_address = sys.argv[2]       #IP Address of printer
        
        print(filename)
        print(ip_address)
        
        send_Pectab_file(filename, ip_address)
        
    except:
        
        print("No file or target entered")         
    