#!/usr/bin/env python3
"""Do cargo sales query for a given date range.

Usage:

    python3 do_skedflexAcftStatus.py <startdate>
"""

import sys
import re
import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta, datetime




def run_query(start_date):
    
    tailNum = []
    acftType = []
    
    statusTailNum = []
    statusCurrent = []
    statusType = []
    
    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)
        
        
        sql = """SELECT aircraft, type FROM Aircraft WHERE active = 'yes' """


        cursor.execute(sql)
        records = cursor.fetchall()
        
        for row in records:
            
            # print(row)
            tailNum.append(row['aircraft'])
            acftType.append(row['type'])
            
        # print(tailNum)
        # print(acftType)
        
        index = 0
        while index < len(tailNum):
            
            sql = """SELECT * FROM SkedFlexTailStatus where startTimes <= %s and endTimes >= %s and names = 'Maintenance' and tails = %s """

            searchTail = tailNum[index]
            statusTailNum.append(searchTail)
            statusCurrent.append('Up')
            statusType.append(acftType[index])
            
            cursor.execute(sql,(start_date, start_date, searchTail))
            records = cursor.fetchall()
        
            if len(records) > 0:
                statusCurrent[index] = 'Down'
               
                
            
            index += 1
            
        # print(statusTailNum)
        # print(statusCurrent)
        # print(statusType)
        
        jsonList = []
        jsonLine = ''
        
        index = 1
        
        while index < len(statusTailNum):
            jsonLine='{"Aircraft":"'+statusTailNum[index]+'","Type":"'+statusType[index]+'","Status":"'+statusCurrent[index]+'"}'
              
                
            jsonList.append(jsonLine)
            
            index += 1

        jsonOutput=str(jsonList)
        
        jsonOutput=jsonOutput.translate({ord("'"):None})
        jsonOutput=jsonOutput.replace("}, {","},{")    
        
        print(jsonOutput)
    

    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        
        


if __name__ == '__main__':
    
    try:   
        start_date = sys.argv[1]
    except:
        start_date = date.today()
     
     
    # print('start_date ',start_date)
    run_query(start_date) 