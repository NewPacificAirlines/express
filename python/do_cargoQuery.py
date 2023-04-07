#!/usr/bin/env python3
"""Do cargo sales query for a given date range.

Usage:

    python3 do_cargoQuery.py <startdate> <enddate>
"""

import sys
import re
import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta, datetime



def run_query(start_date, end_date):

    jsonList = []
    
    station = []
    datePaid = []
    dateRcvd = []
    origin = []
    destination = []
    freightType = []
    payment = []
    subtotal = []
    tax = []
    total = []
    weight = []
    whiz = []
    awb = []
    acctInfo = []
    remarks = []
    

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)


        sql = """SELECT Station, Date_Paid, Date_Received, From_Location, To_Location, Freight_Type, Payment_Type, SubTotal, Tax, Total_Cost, Total_Weight, Payment_ID, AirwayBill_Num, 
        
        Accounting_Info, Remarks FROM Freight_Current WHERE """
        
      
        sql += """(Date_Received BETWEEN %s AND %s) AND Authorized = True AND Freight_Type <> 'Mail' AND Freight_Type <> '' AND Freight_Type <> 'COMAT'"""

        params = (start_date,end_date)

        # print('sql ',sql)
        # print('params ', params)


        cursor.execute(sql, params)
        records = cursor.fetchall()
        # print(len(records))
               
        for row in records:
            
            try:
                station.append(row['Station'])
            except:
                station.append('')
            
            try:  
                
                dateField = row['Date_Paid']
                date_time = dateField.strftime("%m/%d/%Y")
                datePaid.append(date_time)     
                
            except:
                datePaid.append('')
                
            try:     
                dateField = row['Date_Received']
                date_time = dateField.strftime("%m/%d/%Y")
                dateRcvd.append(date_time)     
            except:
                dateRcvd.append('')
            
            try:     
                origin.append(row['From_Location'])
            except:
                origin.append('')
            
            try: 
                destination.append(row['To_Location'])
            except:
                destination.append('')
            
            try: 
                freightType.append(row['Freight_Type'])
            except:
                freightType.append('')
        
            try: 
                payment.append(row['Payment_Type'])
            except:
                payment.append('')
    
            try: 
                subtotal.append(str(row['SubTotal']))
            except:
                subtotal.append('')

            try: 
                tax.append(str(row['Tax']))
            except:
                tax.append('')

            try: 
                total.append(str(row['Total_Cost']))
            except:
                total.append('')

            try: 
                weight.append(str(row['Total_Weight']))
            except:
                weight.append('')

            try: 
                whiz.append(str(row['Payment_ID']))
            except:
                whiz.append('')

            try: 
                awb.append(str(row['AirwayBill_Num']))
            except:
                awb.append('')

            try: 
                acctInfo.append(row['Accounting_Info'])
            except:
                acctInfo.append('')

            try: 
                remarks.append(re.escape(row['Remarks']))
            except:
                remarks.append('')
            
           
           
            

    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    
    
   

    
    # print(station)
    # print(datePaid)
    # print(dateRcvd)
    # print(origin)
    # print(destination)
    # print(freightType)
    # print(payment)
    # print(subtotal)
    # print(tax)
    # print(total)
    # print(weight)
    # print(whiz)
    # print(awb)
    # print(acctInfo)
    # print(remarks)

    # print(len(station))
    # print(len(datePaid))
    # print(len(dateRcvd))
    # print(len(origin))
    # print(len(destination))
    # print(len(freightType))
    # print(len(payment))
    # print(len(subtotal))
    # print(len(tax))
    # print(len(total))
    # print(len(weight))
    # print(len(whiz))
    # print(len(awb))
    # print(len(acctInfo))
    # print(len(remarks))

    index = 0
    
    while index < len(station):
        jsonLine='{"Station":"'+station[index]+'","Date Paid":"'+datePaid[index]+'","Date Rcvd":"'+dateRcvd[index]+'","Origin":"'+origin[index]+'","Destination":"'+destination[index]+'","Type":"'+freightType[index]+'","Payment":"'+payment[index]+\
                        '","Subtotal":"'+subtotal[index]+'","Tax":"'+tax[index]+'","Total":"'+total[index]+'","Weight":"'+weight[index]+'","Whiz":"'+whiz[index]+'","AWB":"'+awb[index]+'"}'
              
                
        jsonList.append(jsonLine)
        
        index += 1

    jsonOutput=str(jsonList)
    # print(jsonOutput)

    jsonOutput=jsonOutput.translate({ord("'"):None})
    jsonOutput=jsonOutput.replace("}, {","},{")    
    
    print(jsonOutput)
    
    
    
if __name__ == '__main__':
    
    try:   
        start_date = sys.argv[1]
    except:
        start_date = ''
     
    try:    
        end_date = sys.argv[2]
    except:
        end_date = ''
        
   
    
    
    # print('start_date ',start_date)
    # print('end_date ',end_date)
    run_query(start_date,end_date) 