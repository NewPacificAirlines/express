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




def run_query(start_date, end_date):
    
    
    tailNum = []
    acftType = []
    
    statusTailNum = []
    statusCurrent = []
    statusType = []
    statusDate = []
    statusNote = []
    
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
        # print('status ',statusCurrent)
        
        
        index = 0
        while index < len(tailNum):
            
            searchTail = tailNum[index]
            statusTailNum.append(searchTail)
            statusCurrent.append('Up')
            statusType.append(acftType[index])
            statusDate.append(start_date)
            statusNote.append('')
            
            sql = """SELECT * FROM SkedFlexTailStatus WHERE startTimes <= """
            
            sql += "'"+start_date+"T11:01:00'"
            sql += """ AND endTimes >= """
            sql += "'"+end_date+"T07:59:00'"
            sql += """ AND names = 'Maintenance' AND tails = """
            sql += "'"+searchTail+"'"
            
            # print('sql ',sql)
            
            
            cursor.execute(sql)
            records = cursor.fetchall()
            
            # print(start_date)
            # print(searchTail)
            # print('records ',len(records))
            # print(len(records))
            
            for row in records:
            
          
                statusCurrent[index] = 'Down'
                statusNote[index] = row['notes']
                
            
            index += 1
            
        # print(statusTailNum)
        # print(statusCurrent)
        # print(statusType)
        # print('notes ',statusNote)
        
        jsonList = []
        jsonLine = ''
        
        index = 0
        
        while index < len(statusTailNum):
            jsonLine='{"Aircraft":"'+statusTailNum[index]+'","Type":"'+statusType[index]+'","Status":"'+statusCurrent[index]+'","Note":"'+statusNote[index]+'","Date":"'+statusDate[index]+'"}'
              
                
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
     
    try:   
        end_date = sys.argv[2]
    except:
        end_date = date.today() 
     
    # print('start_date ',start_date)
    # print('end_date ',end_date)

    run_query(start_date,end_date) 