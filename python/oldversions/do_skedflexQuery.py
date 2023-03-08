#!/usr/bin/env python3
"""Do skedflex query for a given date range.

Usage:

    python3 do_skedflexQuery.py <startdate> <enddate>
"""


import sys
import ast
from telnetlib import SE
import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta, datetime
import dateutil.parser
import re




def run_query(start_date, end_date, flight_num,tails):
    

    # print(start_date)
    # print(end_date)
    # print(flight_num)
    # print(tail_num)
    
    IDs = []
    Dates = []
    SchedDeps = []
    SchedArvs = []
    FlightNums = []
    Statuses = []
   
    Tails = []
    Seats = []
    OutTimes = []
    OffTimes = []
    OnTimes = []
    InTimes = []
    DepartLocs = []
    ArriveLocs = []
    DepartDelayCodes = []
    DepartDelayTimes =[]
    Captain = []
    
    Types = []
    OpsTypes = []
    Canceleds = []
    IrregularCodes = []
    DateTimeStamp = []
    Pax = []
    Cargo = []
    Mail = []
    MailNon = []
    Bags = []
    rpms = []
    asms = []
    PaxNon = []
    Rush = []
    Comat = []
    BagCount = []
    Copilot = []
    FlightAttendant = []
    fob = []
    burn =[]
    
    connection = 0


    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)
        
       
        sql = """SELECT id, flightNum, status, date, tail, eqp, schedDepTime, schedArvTime, outTime, offTime, onTime, inTime, departLoc, arriveLoc, departDelays, crew, type, opsTypes, irregularCode, seats, pax, paxnon, cargo, rush, comat, mail, mailnon, bags, bagcount, rpm, asm, fob, burn FROM SkedFlexData
                WHERE (date BETWEEN %s AND %s) AND type <> 'offline-dh' AND status <> 'deleted'"""
        
        params = (start_date, end_date)
        
        # print(type(params))
        
        if(flight_num != ''):
                            
            sql += """ AND flightNum = %s"""
            params = params + (flight_num,)
            
        if(tails != ''):
            tails_sql = ''
            
            tails_list = tails.split(",")    
            tails_sql += " AND ("
            # print(tails_list)
            
            for i in tails_list:
                tails_sql += " tail LIKE '%"+i+"%' OR "
                
            tails_sql = tails_sql[:-4]
            tails_sql += ") " 
            sql += tails_sql
            
        # sql += " ORDER BY date, flightNum"
        
        
        # print(sql)
        # print(params)
        # print(type(params))
        
        cursor.execute(sql, params)
        records = cursor.fetchall()
        
        for row in records:
            
            skedID =str((row['id']))
            IDs.append(skedID)
            
            FlightNums.append(row['flightNum'])
            
            status = row['status']
            Statuses.append(status)
            if(status == 'canceled'):
                Canceleds.append('TRUE')
            else:
                Canceleds.append('FALSE')
                        
            # Dates.append(row['date'].strftime('%x'))
            Dates.append(row['date'].strftime('%-m/%-d/%y'))

            try:
                tailDict = ast.literal_eval(row['tail'])
                fullTail = (tailDict.get('tailNumber'))
                Tails.append(re.sub('[^0-9]','', fullTail))
            except:
                Tails.append('')
            try:
                seats = row['seats']
                Seats.append(seats)
                
            except:
                Seats.append(37)
                
            try:
                SchedDeps.append(datetime.strftime(dateutil.parser.parse(row['schedDepTime']),'%H:%M:%S'))
            except:
                SchedDeps.append('')    
                
            try:
                SchedArvs.append(datetime.strftime(dateutil.parser.parse(row['schedArvTime']),'%H:%M:%S'))
            except:
                
                SchedArvs.append('')  
            try:
                OutTimes.append(datetime.strftime(dateutil.parser.parse(row['outTime']),'%H:%M:%S'))
            except:
                OutTimes.append('00:00:00')
                
            try:
                OffTimes.append(datetime.strftime(dateutil.parser.parse(row['offTime']),'%H:%M:%S'))
            except:
                OffTimes.append('00:00:00')
                
            try:
                OnTimes.append(datetime.strftime(dateutil.parser.parse(row['onTime']),'%H:%M:%S'))
            except:
                OnTimes.append('00:00:00')
                
            try:
                InTimes.append(datetime.strftime(dateutil.parser.parse(row['inTime']),'%H:%M:%S'))
            except:
                InTimes.append('00:00:00')
                
            try:
                departLocDict = ast.literal_eval(row['departLoc'])
                DepartLocs.append(departLocDict.get('code'))
            except:
                DepartLocs.append('')
                
            try:
                arriveLocDict = ast.literal_eval(row['arriveLoc'])
                ArriveLocs.append(arriveLocDict.get('code'))
            except:
                ArriveLocs.append('')
            
            try:   
                delayStr = ''
                delayDuration = 0
                departDelaysList = ast.literal_eval(row['departDelays'])
                index = 0
                while index < len(departDelaysList):
                    departDelaysDict = departDelaysList[index]
                    delayStr=delayStr+(departDelaysDict.get('code'))+'|'
                    delayDuration=delayDuration+(departDelaysDict.get('duration'))
                    index += 1 
                DepartDelayCodes.append(delayStr)
                sec = delayDuration * 60
                delayDurationTime = str(timedelta(seconds=sec))                
                DepartDelayTimes.append(delayDurationTime)
            except:
                DepartDelayCodes.append('')
                DepartDelayTimes.append('00:00:00')
                    
                
            try:   

                crewMembers =''
                crewCopilot =''
                crewFlightAttendant =''
                crewObjStr=(row['crew'])
                crewVar = crewObjStr.replace('} {','} , {')
                crewVar = "["+crewVar+"]"
                crewList = ast.literal_eval(crewVar)
                index = 0
                # print(len(crewList))
                while index < len(crewList):
                    crewDict=crewList[index]
                    crewMember=crewDict.get('user')
                    # crewName=crewMember.get('lastName')
                    crewPosition=crewDict.get('position')
                    crewPosName=crewPosition.get('name')
                    crewFull=crewMember.get('nameLastFirst')
                    # print(crewPosName)
                    # print(crewFull)
                    # crewMembers=crewMembers+crewPosName+'-'+crewName+' | '
                    
                    if(crewPosName == "Captain" ) or (crewPosName == "Check Airman"):
                        crewMembers=crewFull
                    if(crewPosName == "First Officer") or (crewPosName == "FO Trainee"):
                        crewCopilot=crewFull
                    if(crewPosName == "Flight Attendant"):
                        crewFlightAttendant=crewFull
                    
                        
                    index += 1
                Captain.append(crewMembers)
                Copilot.append(crewCopilot)
                FlightAttendant.append(crewFlightAttendant)
                
            except:
                Captain.append('')
                Copilot.append('')
                FlightAttendant.append('')
            try:
                opsTypeDict = ast.literal_eval(row['opsTypes'])
                OpsTypes.append(opsTypeDict.get('code'))
            except:
                OpsTypes.append('')
            
            try:
                Types.append(row['type'])
            except:
                Types.append('')
                
            try:
                code=row['irregularCode']
                
                if(code == "01"):
                    code="01 Aircraft Damage"

                elif(code == "02"):
                    code="02 A/C Maint"

                elif(code == "03"):
                    code="03 AWOS out of Service"

                elif(code == "04"):
                    code="04 CREW"

                elif(code == "05"):
                    code="05 Customer Request-Charter"

                elif(code == "06"):
                    code="06 Delete/Duplicate/Test"

                elif(code == "07"):
                    code="07 Originating Flights Late"

                elif(code == "08"):
                    code="08 Runways/Facilities/Nav-Aid"

                elif(code == "09"):
                    code="09 Commercial"

                elif(code == "10"):
                    code="10 Volcanic Ash Forecast"

                elif(code == "11"):
                    code="11 Weather"

                elif(code == "12"):
                    code="12 Signelificant Delay/Consolidation"

                elif(code == "13"):
                    code="13 System Disruption/Consolidation"

                elif(code == "14"):
                    code="14 A/C Availability/Consolidation"
                    
                elif(code == "15"):
                    code="15 Crew/Consolidation"
                        
                elif(code == "16"):
                    code="16 TFR"
                    
                else:
                    code=""
                    
                IrregularCodes.append(code)                
                # IrregularCodes.append(row['irregularCode'])
                
            
            except:
                IrregularCodes.append('')
            
            now = datetime.now()    
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            DateTimeStamp.append(date_time)    
            
            try:
                Pax.append(str(row['pax']))
            except:
                Pax.append('0')
                
            try:
                if str(row['paxnon']) =='None':
                    PaxNon.append('0')
                else:
                    PaxNon.append(str(row['paxnon']))  
            except:
                PaxNon.append('0')
                
            try:
                Cargo.append(str(row['cargo']))
            except:
                Cargo.append('0')
                
            try:
                if str(row['rush']) =='None':
                    Rush.append('0')
                else:
                    Rush.append(str(row['rush']))
            except:
                Rush.append('0')
            
            try:
                if str(row['comat']) =='None':
                    Comat.append('0')
                else:
                    Comat.append(str(row['comat']))
            except:
                Comat.append('0')
                
            try:
                Mail.append(str(row['mail']))
            except:
                Mail.append('0')

            try:
                if str(row['mailnon']) =='None':
                    MailNon.append('0')
                else:
                    MailNon.append(str(row['mailnon']))
            except:
                MailNon.append('0')
                
            try:
                Bags.append(str(row['bags']))
            except:
                Bags.append('0')
                
            try:
                if str(row['bagcount']) =='None':
                    BagCount.append('0')
                else:
                    BagCount.append(str(row['bagcount']))
            except:
                BagCount.append('0')
            
            try:
                rpms.append(str(row['rpm']))
            except:
                rpms.append('0')
                
            try:
                asms.append(str(row['asm']))
            except:
                asms.append('0')
                
            try:
                if str(row['fob']) =='None':
                    fob.append('0')
                else:
                    fob.append(str(row['fob']))
            except:
                fob.append('0')
         
            try:
                if str(row['burn']) =='None':
                    burn.append('0')
                else:
                    burn.append(str(row['burn']))
            except:
                burn.append('0')
                
                
        
    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    
    # print(Canceleds)
    # print(Statuses)
    # print(Dates)
    
    # print(Captain)
    # print(Copilot)
    # print(FlightAttendant)
    
    # print(len(Types))
    # print(len(OpsTypes))
    # print(len(Canceleds))
    # print(Pax)
    # print(Cargo)
    # print('Mail Totals')
    # print(Mail)
    # print('NonPri totals')
    # print(MailNon)
    # print(Bags)
    # print(rpms)
    # print(asms)
    # print(len(Pax))
    # print(len(Cargo))
    # print(len(Mail))
    # print(len(Bags))
    # print(len(rpms))
    # print(len(asms))

    
    jsonList=[]   
    index = 0
    while index < len(FlightNums):
        jsonLine='{"ID":"'+IDs[index]+'","FltDate":"'+Dates[index]+'","SkedDep":"'+SchedDeps[index]+'","FltNumber":"'+ FlightNums[index]+'","Status":"'+ Statuses[index]+\
            '","Acft":"'+Tails[index]+'","Seats":"'+str(Seats[index])+'","Out":"'+OutTimes[index]+'","Off":"'+OffTimes[index]+\
            '","On":"'+OnTimes[index]+'","In":"'+InTimes[index]+'","SkedArr":"'+SchedArvs[index]+'","Origin":"'+DepartLocs[index]+\
            '","Dest":"'+ArriveLocs[index]+'","DelayTime":"'+DepartDelayTimes[index]+'","DelayData":"'+DepartDelayCodes[index]+\
            '","Captain":"'+Captain[index]+'","Copilot":"'+Copilot[index]+'","Flight Attendant":"'+FlightAttendant[index]+\
            '","SkedFlexType":"'+Types[index]+'","SkedFlexOpsType":"'+OpsTypes[index]+'","Canceled":"'+Canceleds[index]+\
            '","CanceledReason":"'+IrregularCodes[index]+'","DateTimeStamp":"'+DateTimeStamp[index]+'","Pax":"'+Pax[index]+'","PaxNon":"'+PaxNon[index]+\
            '","Rush":"'+Rush[index]+'","Comat":"'+Comat[index]+'","BagCount":"'+BagCount[index]+'","FOB":"'+fob[index]+'","Burn":"'+burn[index]+\
            '","Cargo":"'+Cargo[index]+'","Mail":"'+Mail[index]+'","MailNon":"'+MailNon[index]+'","Bags":"'+Bags[index]+'","RPM":"'+rpms[index]+'","ASM":"'+asms[index]+'"}'
        
        jsonList.append(jsonLine)
        
        index += 1
    jsonOutput=str(jsonList)
    # print(jsonOutput)

    jsonOutput=jsonOutput.translate({ord("'"):None})
    jsonOutput=jsonOutput.replace("}, {","},{")    
    jsonOutput=jsonOutput.replace("|"," ")
    
    print(jsonOutput)
    # return(jsonOutput)

    # print(start_date)
    # print(end_date)    
    # print(flight_num)
    # print(tail_num)    
    # # print(type(flight_num))
    # print(type(tail_num))    


if __name__ == '__main__':
    
    

    try:    
        end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
    except:
        end_date = date.today()
        
    try:   
        start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')    #The 0th arg is the module filename.
    except:
        start_date = end_date-timedelta(days=7)
    
    try:    
        flight_num = sys.argv[3]
    except:
        flight_num = ''
    
    try:        
        tails = sys.argv[4]
    except:
        tails = ''
        
        
    # print(start_date)
    # print(end_date)    
    # print(flight_num)
    # print(tail_num)    
    # print(tails)
       
    run_query(start_date,end_date,flight_num,tails) 