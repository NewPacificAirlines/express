#!/usr/bin/env python3
"""Find printer IP address based on name.

Usage:

    python3 find_Printer.py <name> 
"""


import sys
import mysql.connector
from mysql.connector import Error


def find_printer(name):
    
    # print(name)
    
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)
        
        sql = """SELECT ip_address FROM Printers WHERE name = %s"""
        
        params = (name,)
        
        # print(type(params))
        
        cursor.execute(sql, params)
        records = cursor.fetchall()
        
        for row in records:
            address = row['ip_address']
        
        # print('ip address is ',address)
        return(address)
    
    except:

        print('Error occured')  
    
if __name__ == '__main__':
       
    try:
        printer = sys.argv[1]       #Printer name 
        
        # print(printer)
        
        find_printer(printer)
        
    except:
        
        print('error no printer name!')
        
        
