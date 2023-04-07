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
    
    
    AWB_Num = []
    Agent_Rcvd = []
    ChargeableWeight = []
    Destination = []
    FlatRate = []
    FlightNumber = []
    Freight_ID = []
    Freight_ItemsID = []
    Frt_Type = []
    FrtRate = []
    FrtSeqNum = []
    Handle_Fees = []
    Item_Number = []
    Load_Location = []
    MustRide = []
    Origin = []
    Pieces = []
    RateType = []
    Remarks = []
    Shipper = []
    SyncUUID = []
    Tax = []
    Total_Due = []
    Weight = []

    
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
        
        sql = """SELECT * FROM Freight_Items where AWB_Num = %s 
        """

        cursor.execute(sql, params)
        records = cursor.fetchall()
        
        for row in records:
            
            # print('row data ',row)
            
            try:
                AWB_Num.append(str(row['AWB_Num']))

            except:
                AWB_Num.append('')
                
            try:
                Agent_Rcvd.append(row['Agent_Rcvd'])

            except:
                Agent_Rcvd.append('')
                
            try:
                ChargeableWeight.append(str(int(row['ChargeableWeight'])))

            except:
                ChargeableWeight.append('')
                
            try:
                Destination.append(row['Destination'])

            except:
                Destination.append('')
                
            try:
                if row['FlatRate'] == 1:
                    FlatRate.append('Yes')
                else:
                    FlatRate.append('No')
            except:
                FlatRate.append('No')
                
            try:
                FlightNumber.append(str(row['FlightNumber']))

            except:
                FlightNumber.append('')
                
            try:
                Freight_ID.append(str(row['Freight_ID']))

            except:
                Freight_ID.append('')
                
            try:
                Freight_ItemsID.append(str(row['Freight_ItemsID']))

            except:
                Freight_ItemsID.append('')
                
            try:
                Frt_Type.append(row['Frt_Type'])

            except:
                Frt_Type.append('')
                
            try:
                FrtRate.append(str(row['FrtRate']))

            except:
                FrtRate.append('')
                
            try:
                FrtSeqNum.append(row['FrtSeqNum'])

            except:
                FrtSeqNum.append('')
                
            try:
                Handle_Fees.append(str(row['Handle_Fees']))

            except:
                Handle_Fees.append('')
                
            try:
                Item_Number.append(row['Item_Number'])

            except:
                Item_Number.append('')
                
            try:
                Load_Location.append(row['Load_Location'])

            except:
                Load_Location.append('')
                
            try:
                if row['MustRide'] == 1:
                        MustRide.append('Yes')
                else:
                    MustRide.append('No')
            except:
                MustRide.append('No')
            
            try:
                Origin.append(row['Origin'])

            except:
                Origin.append('')
                
            try:
                Pieces.append(str(int(row['Pieces'])))

            except:
                Pieces.append('')
                
            try:
                RateType.append(row['RateType'])

            except:
                RateType.append('')
                
            try:
                Remarks.append(row['Remarks'])

            except:
                Remarks.append('')
                
            try:
                Shipper.append(row['Shipper'])

            except:
                Shipper.append('')
                
            try:
                SyncUUID.append(row['SyncUUID'])

            except:
                SyncUUID.append('')
                
            try:
                Tax.append("{:,.2f}".format(row['Tax']))

            except:
                Tax.append('')
                
            try:
                Total_Due.append("{:,.2f}".format(row['Total_Due']))

            except:
                Total_Due.append('')
                
            try:
                Weight.append(str(int(row['Weight'])))

            except:
                Weight.append('')

    
    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
  
        # print('AWB_Num',type(AWB_Num[0]))
        # print('Agent_Rcvd',type(Agent_Rcvd[0]))
        # print('ChargeableWeight',type(ChargeableWeight[0]))
        # print('Destination',type(Destination[0]))
        # print('FlatRate',type(FlatRate[0]))
        # print('FlightNumber',type(FlightNumber[0]))
        # print('Freight_ID',type(Freight_ID[0]))
        # print('Freight_ItemsID',type(Freight_ItemsID[0]))
        # print('Frt_Type',type(Frt_Type[0]))
        # print('FrtRate',type(FrtRate[0]))
        # print('FrtSeqNum',type(FrtSeqNum[0]))
        # print('Handle_Fees',type(Handle_Fees[0]))
        # print('Item_Number',type(Item_Number[0]))
        # print('Load_Location',type(Load_Location[0]))
        # print('MustRide',type(MustRide[0]))
        # print('Origin',type(Origin[0]))
        # print('Pieces',type(Pieces[0]))
        # print('RateType',type(RateType[0]))
        # print('Remarks',type(Remarks[0]))
        # print('Shipper',type(Shipper[0]))
        # print('SyncUUID',type(SyncUUID[0]))
        # print('Tax',type(Tax[0]))
        # print('Total_Due',type(Total_Due[0]))
        # print('Weight',type(Weight[0]))


        # print(AWB_Num)
        # print(Agent_Rcvd)
        # print(ChargeableWeight)
        # print(Destination)
        # print(FlatRate)
        # print(FlightNumber)
        # print(Freight_ID)
        # print(Freight_ItemsID)
        # print(Frt_Type)
        # print(FrtRate)
        # print(FrtSeqNum)
        # print(Handle_Fees)
        # print(Item_Number)
        # print(Load_Location)
        # print(MustRide)
        # print(Origin)
        # print(Pieces)
        # print(RateType)
        # print(Remarks)
        # print(Shipper)
        # print(SyncUUID)
        # print(Tax)
        # print(Total_Due)
        # print(Weight)



          
          
    index = 0
    # print(len(records))
    jsonLine = ''

    while index < len(AWB_Num):
        
    
        jsonLine='{"AWB_Num":"'+AWB_Num[index]+'","Agent_Rcvd":"'+Agent_Rcvd[index]+'","ChargeableWeight":"'+ChargeableWeight[index]+\
            '","Destination":"'+Destination[index]+'","FlatRate":"'+FlatRate[index]+'","FlightNumber":"'+FlightNumber[index]+\
            '","Freight_ID":"'+Freight_ID[index]+'","Freight_ItemsID":"'+Freight_ItemsID[index]+'","Frt_Type":"'+Frt_Type[index]+\
            '","FrtRate":"'+FrtRate[index]+'","FrtSeqNum":"'+FrtSeqNum[index]+'","Handle_Fees":"'+Handle_Fees[index]+\
            '","Item_Number":"'+Item_Number[index]+'","Load_Location":"'+Load_Location[index]+'","MustRide":"'+MustRide[index]+\
            '","Origin":"'+Origin[index]+'","Pieces":"'+Pieces[index]+'","RateType":"'+RateType[index]+'","Remarks":"'+Remarks[index]+\
            '","Shipper":"'+Shipper[index]+'","SyncUUID":"'+SyncUUID[index]+'","Tax":"'+Tax[index]+'","Total_Due":"'+Total_Due[index]+'","Weight":"'+Weight[index]+'"}'
        
        jsonList.append(jsonLine)
        
        index += 1
    
    
    
    
    jsonOutput=str(jsonList)
    # print(jsonOutput)

    jsonOutput=jsonOutput.translate({ord("'"):None})
    jsonOutput=jsonOutput.replace("}, {","},{")    
    jsonOutput=jsonOutput.replace("|"," ")
    
    print(jsonOutput)
    # return(jsonOutput)


if __name__ == '__main__':
    
   
 
    try:   
        id = sys.argv[1]  #The 0th arg is the module filename.
        
        # print(id)
  
        run_query(id) 

    except:
        print("error no id given")
    
 
        
   
