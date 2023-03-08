#!/usr/bin/env python3
"""Do manifest query for a given date range.

Usage:

    python3 do_manifestQuery.py <startdate> <enddate>
"""

import sys
import ast
from telnetlib import SE
import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta, datetime
import dateutil.parser
import re


def run_query(start_date, end_date, id):
    
   
    # print('start_date ',start_date)
    # print('end_date ',end_date)

    jsonList = []
    
    manifestID = []
    skedflexID = []
    date = []
    tail = []
    flight = []
    origin = []
    dest = []
    name = []
    infant = []
    ticket = []
    revenue = []
    seat = []
    remark = []
    bagcount = []
    bagweight = []
    itemtype = []
    cargoweight = []
    cargoAWB = []
    cargopieces = []


    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)


        sql = """SELECT skedflexID, manifestID, date, tail, flight, origin, dest, name, infant, ticket, type, revenue, seats, remarks, bagcount, 
        bagweight, cargotype, cargopieces, cargoweight, cargoAWB, cargo_origin, cargo_dest FROM Manifests WHERE """
        
        if(start_date != ''):
            
            sql += """(date BETWEEN %s AND %s) """

            params = (start_date,end_date)

        else:
            
            sql += """skedflexID = %s"""
            
            params = (id,)

        # print('sql ',sql)
        # print('params ', params)


        cursor.execute(sql, params)
        records = cursor.fetchall()
        # print(len(records))
               
        for row in records:
            
            try:
                manifestID.append(row['manifestID'])
            except:
                manifestID.append('')
            
            try:    
                skedflexID.append(str(row['skedflexID']))
            except:
                skedflexID.append('')
                
            try:     
                date.append(row['date'])
            except:
                date.append('')
            
            try:     
                tail.append(row['tail'])
            except:
                tail.append('')
            
            try: 
                flight.append(row['flight'])
            except:
                flight.append('')
            
            try:     
                if row['origin'] is None: 
                    if row['cargo_origin'] is not None:
                         origin.append(row['cargo_origin'])
                    else:
                        origin.append('')
                else:
                    origin.append(row['origin'])
            except:
                origin.append('')
            
            try:     
                if row['dest'] is None:   
                    if row['cargo_dest'] is not None:
                         dest.append(row['cargo_dest'])     
                    else: 
                        dest.append('')
                else:   
                    dest.append(row['dest'])
            except:
                dest.append('')
            
            try:       
                if row['name'] is None:        
                    name.append('')
                else:
                    name.append(row['name'])
            except:
                name.append('')
                
            try:       
                if row['type'] is None: 
                    if row['cargotype'] is not None:    
                           itemtype.append(row['cargotype'])
                    else:
                        itemtype.append('')
                else:
                    itemtype.append(row['type'])
            except:
                itemtype.append('')    
            
            try: 
                
                if row['infant'] is None:        
                    infant.append('')
                else:
                    infant.append(row['infant'])
            except:
                infant.append('')
            
            try:     
                if row['ticket'] is None:        
                    ticket.append('')
                else:
                    ticket.append(row['ticket'])
            except:
                ticket.append('')
            
            try:     
                if row['revenue'] is None:        
                    revenue.append('')
                else:
                    revenue.append(row['revenue'])
            except:
                revenue.append('')
            
            try:     
                if row['seats'] is None:        
                    seat.append('')
                else:
                    seat.append(row['seats'])
            except:
                seat.append('')
            
            try:         
                if row['remarks'] is None:        
                    remark.append('')
                else:
                    remark.append(row['remarks'])
            except:
                remark.append('')
            
            try:     
                if row['bagcount'] is None:        
                    bagcount.append('')
                else:
                    bagcount.append(str(row['bagcount']))
            except:
                bagcount.append('')
            
            try: 
                if row['bagweight'] is None:        
                    bagweight.append('')
                else:
                    bagweight.append(str(row['bagweight']))
            except:
                bagweight.append('')
            
            try:     
                if row['cargopieces'] is None:        
                    cargopieces.append('')
                else:
                    cargopieces.append(str(row['cargopieces']))
            except:
                cargopieces.append('')
            
            try:     
                if row['cargoweight'] is None:        
                    cargoweight.append('')
                else:
                    cargoweight.append(str(row['cargoweight']))
            except:
                cargoweight.append('')
            
            try:     
                if row['cargoAWB'] is None:        
                    cargoAWB.append('')
                else:
                    cargoAWB.append(row['cargoAWB'])
            except:
                cargoAWB.append('')
            
           
            

    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    index = 0
    
    
    # print('manifestID',manifestID)
    # print('skedflexID',skedflexID)
    # print('date',date)
    # print('tail',tail)
    # print('flight',flight)
    # print('origin',origin)
    # print('dest',dest)
    # print('name',name)
    # print('infant',infant)
    # print('ticket',ticket)
    # print('itemtype',itemtype)
    # print('revenue',revenue)
    # print('seat',seat)
    # print('remark',remark)
    # print('bagcount',bagcount)
    # print('bagweight',bagweight)
    # print('cargoweight',cargoweight)
    # print('cargoAWB',cargoAWB)
    
    # print('manifestID',len(manifestID))
    # print('skedflexID',len(skedflexID))
    # print('date',len(date))
    # print('tail',len(tail))
    # print('flight',len(flight))
    # print('origin',len(origin))
    # print('dest',len(dest))
    # print('name',len(name))
    # print('infant',len(infant))
    # print('ticket',len(ticket))
    # print('itemtype',len(itemtype))
    # print('revenue',len(revenue))
    # print('seat',len(seat))
    # print('remark',len(remark))
    # print('bagcount',len(bagcount))
    # print('bagweight',len(bagweight))
    # print('cargoweight',len(cargoweight))
    # print('cargopieces',len(cargopieces))
    # print('cargoAWB',len(cargoAWB))

    
    # print('Records',len(manifestID))
    
    while index < len(manifestID):
        jsonLine='{"ID":"'+manifestID[index]+'","SkedFlexID":"'+skedflexID[index]+'","Date":"'+date[index]+'","Tail":"'+tail[index]+'","Flight":"'+flight[index]+'","Origin":"'+origin[index]+'","Dest":"'+dest[index]+\
            '","Name":"'+name[index]+'","Infant":"'+infant[index]+'","Ticket":"'+ticket[index]+'","Type":"'+itemtype[index]+'","RevFlag":"'+revenue[index]+'","Seat":"'+seat[index]+'","Remarks":"'+remark[index]+\
            '","BagCount":"'+bagcount[index]+'","BagWeight":"'+bagweight[index]+'","CargoWeight":"'+cargoweight[index]+\
            '","CargoPieces":"'+cargopieces[index]+'","CargoAWB":"'+cargoAWB[index]+'"}'
              
                
        jsonList.append(jsonLine)
        
        index += 1

    jsonOutput=str(jsonList)
    # print(jsonOutput)

    jsonOutput=jsonOutput.translate({ord("'"):None})
    jsonOutput=jsonOutput.replace("}, {","},{")    
    
    print(jsonOutput)
    # print('manifestIDs ',manifestIDs)


if __name__ == '__main__':
    
    try:   
        start_date = sys.argv[1]
    except:
        start_date = ''
     
    try:    
        end_date = sys.argv[2]
    except:
        end_date = ''
        
   
    try: 
        id = sys.argv[3]
    except:
        id= ''

    
    # print('start_date ',start_date)
    # print('end_date ',end_date)
    # print('id ',id)
    run_query(start_date,end_date,id) 