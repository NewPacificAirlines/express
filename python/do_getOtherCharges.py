#!/usr/bin/env python3
"""Do cargo records query for a given date range or origin and dest.

Usage:

    python3 do_cargoDataQuery.py <startdate> <enddate> <origin> <dest>
"""

import sys
import re
import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta, datetime
import dateutil.parser
import json


def run_query(id):    
    
    jsonList = []
    otherCharges = []
    
    id = '000'+id
    # print('Freight_ID',id)
    # print('Type ',type(id))
    
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)
        
        params = (id,)
        
        sql = """SELECT OtherCharges FROM Freight_Current where AirwayBill_Num = %s 
        """

        cursor.execute(sql, params)
        records = cursor.fetchall()
        
        for row in records:
            # print(row)
            try:
                OtherCharges = str(row(['Othercharges']))
                if (OtherCharges == ''):
                    otherCharges.append('{"Amount": "0", "Description": "", "Taxable": "", "ChargeDue": ""}')
                else:
                    otherCharges.append(str(row['OtherCharges']))

            except:
                otherCharges.append('{"Amount": "0", "Description": "", "Taxable": "", "ChargeDue": ""}')
   
        
       
     
    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
    index = 0
    # print(len(records))
    jsonLine = ''

    while index < len(otherCharges):
        
    
        jsonLine=otherCharges[index]
        index += 1    
    
    jsonList.append(jsonLine)
        
    jsonOutput=str(jsonList)
    # print(jsonOutput)

    jsonOutput=jsonOutput.translate({ord("'"):None})
    jsonOutput=jsonOutput.replace("}, {","},{")    
    jsonOutput=jsonOutput.replace("|"," ")
    jsonOutput=jsonOutput.replace("[[","[")
    jsonOutput=jsonOutput.replace("]]","]")
    print(jsonOutput)
    # return(jsonOutput)
    
if __name__ == '__main__':
    
   
 
    try:   
        id = sys.argv[1]  #The 0th arg is the module filename.
        
        # print(id)
  
        run_query(id) 

    except:
        print("error no id given")
    