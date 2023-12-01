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
from pytz import timezone



def run_query(start_date, end_date,utc):
    
    
    
    
    Dates = []
    
    SchedDeps = []
    SchedArvs = []
    OutTimes = []
    OffTimes = []
    OnTimes = []
    InTimes = []

    SchedDepTimes = []
    SchedArvTimes = []
    OutTimeTimes = []
    OffTimeTimes = []
    OnTimeTimes = []
    InTimeTimes = []

    
    FlightNums = []
    Statuses = []
   
    Tails = []
    Seats = []
    DepartLocs = []
    ArriveLocs = []
    DepartDelayCodes = []
    DepartDelayTimes =[]
    Crews = []
    
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
    
    
    

    connection = 0
   
    format_string = '%Y-%m-%dT%H:%M:%S%z'

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)
        
        # sql = """SELECT flightNum, status, date, tail, eqp, schedDepTime, schedArvTime, outTime, offTime, onTime, inTime, departLoc, arriveLoc, departDelays, crew, type, opsTypes, irregularCode, seats, pax, cargo, mail, bags, rpm, asm FROM SkedFlexData
        #         WHERE (date BETWEEN %s AND %s) AND type <> 'offline-dh' AND status <> 'deleted' AND status <> 'canceled' AND (opsTypes LIKE '%SCHED%' OR opsTypes LIKE '%CHARTER%') ORDER BY flightNum """
                        
        sql = """SELECT flightNum, status, date, tail, eqp, schedDepTime, schedArvTime, outTime, offTime, onTime, inTime, departLoc, arriveLoc, departDelays, crew, type, opsTypes, irregularCode, seats, pax, cargo, mail, mailnon, bags, rpm, asm FROM SkedFlexData
                WHERE (date BETWEEN %s AND %s) AND type <> 'offline-dh' AND status <> 'deleted' AND (opsTypes LIKE '%SCHED%' OR opsTypes LIKE '%XTRASECT%' ) ORDER BY date, flightNum """


        cursor.execute(sql, (start_date, end_date))
        records = cursor.fetchall()
        
        for row in records:
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

            
            if utc == 'yes':
            
            
                try:
                    SchedDeps.append(str(row['schedDepTime']))
                except:
                    SchedDeps.append('')    
                    
                try:
                    SchedArvs.append(str(row['schedArvTime']))
                except:
                    
                    SchedArvs.append('')  
                try:
                    OutTimes.append(str(row['outTime']))
                except:
                    OutTimes.append('00:00:00')
                    
                try:
                    OffTimes.append(str(row['offTime']))
                except:
                    OffTimes.append('00:00:00')
                    
                try:
                    OnTimes.append(str(row['onTime']))
                except:
                    OnTimes.append('00:00:00')
                    
                try:
                    InTimes.append(str(row['inTime']))
                except:
                    InTimes.append('00:00:00')
                
            else:
                
                
                try:
                    origTime = datetime.strptime(row['schedDepTime'],format_string)
                    convertedTime = origTime.astimezone(timezone('America/Anchorage'))
                    newTime = str(convertedTime)
                    truncatedTime = newTime[11:19]
                    SchedDeps.append(truncatedTime)
                except:
                    SchedDeps.append('')    
                    
                try:
                    origTime = datetime.strptime(row['schedArvTime'],format_string)
                    convertedTime = origTime.astimezone(timezone('America/Anchorage'))
                    newTime = str(convertedTime)
                    truncatedTime = newTime[11:19]
                    SchedArvs.append(truncatedTime)
                except:
                    SchedArvs.append('')  
                    
                try:
                    origTime = datetime.strptime(row['outTime'],format_string)
                    convertedTime = origTime.astimezone(timezone('America/Anchorage'))
                    newTime = str(convertedTime)
                    truncatedTime = newTime[11:19]
                    OutTimes.append(truncatedTime)
                except:
                    OutTimes.append('00:00:00')
                    
                try:
                    origTime = datetime.strptime(row['offTime'],format_string)
                    convertedTime = origTime.astimezone(timezone('America/Anchorage'))
                    newTime = str(convertedTime)
                    truncatedTime = newTime[11:19]
                    OffTimes.append(truncatedTime)
                except:
                    OffTimes.append('00:00:00')
                    
                try:
                    origTime = datetime.strptime(row['onTime'],format_string)
                    convertedTime = origTime.astimezone(timezone('America/Anchorage'))
                    newTime = str(convertedTime)
                    truncatedTime = newTime[11:19]
                    OnTimes.append(truncatedTime)
                except:
                    OnTimes.append('00:00:00')
                    
                try:
                    origTime = datetime.strptime(row['inTime'],format_string)
                    convertedTime = origTime.astimezone(timezone('America/Anchorage'))
                    newTime = str(convertedTime)
                    truncatedTime = newTime[11:19]
                    InTimes.append(truncatedTime)
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

                crewMembers=''
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
                    
                    if(crewPosName == "Captain"):
                        crewMembers=crewFull
                    
                        
                    index += 1
                Crews.append(crewMembers)
                
            except:
                Crews.append('')

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
                Pax.append('')
                
            try:
                Cargo.append(str(row['cargo']))
            except:
                Cargo.append('')
            
            try:
                Mail.append(str(row['mail']))
            except:
                Mail.append('')

            try:
                MailNon.append(str(row['mailnon']))
            except:
                MailNon.append('')
                
                
            try:
                Bags.append(str(row['bags']))
            except:
                Bags.append('')

            try:
                rpms.append(str(row['rpm']))
            except:
                rpms.append('')
                
            try:
                asms.append(str(row['asm']))
            except:
                asms.append('')
                
        
    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
    
    
    # print(Canceleds)
    # print(Statuses)

    # print(Dates)
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
    
    # print(SchedDepTimes)
    # print(SchedArvTimes)
    # print(OutTimeTimes)
    # print(OffTimeTimes)
    # print(OnTimeTimes)
    # print(InTimeTimes)


    jsonList=[]   
    index = 0
    while index < len(FlightNums):
            
        jsonLine='{"FltDate":"'+Dates[index]+'","SkedDep":"'+SchedDeps[index]+'","FltNumber":"'+ FlightNums[index]+\
            '","Acft":"'+Tails[index]+'","Seats":"'+str(Seats[index])+'","Out":"'+OutTimes[index]+'","Off":"'+OffTimes[index]+\
            '","On":"'+OnTimes[index]+'","In":"'+InTimes[index]+'","SkedArr":"'+SchedArvs[index]+'","Origin":"'+DepartLocs[index]+\
            '","Dest":"'+ArriveLocs[index]+'","DelayTime":"'+DepartDelayTimes[index]+'","DelayData":"'+DepartDelayCodes[index]+\
            '","Captain":"'+Crews[index]+'","SkedFlexType":"'+Types[index]+'","SkedFlexOpsType":"'+OpsTypes[index]+'","Canceled":"'+Canceleds[index]+\
            '","CanceledReason":"'+IrregularCodes[index]+'","DateTimeStamp":"'+DateTimeStamp[index]+'","Pax":"'+Pax[index]+\
            '","Cargo":"'+Cargo[index]+'","Mail":"'+Mail[index]+'","MailNon":"'+MailNon[index]+'","Bags":"'+Bags[index]+'","RPM":"'+rpms[index]+'","ASM":"'+asms[index]+'"}'
            
        jsonList.append(jsonLine)
        
        index += 1
    jsonOutput=str(jsonList)
    # print(jsonOutput)

    jsonOutput=jsonOutput.translate({ord("'"):None})
    jsonOutput=jsonOutput.replace("}, {","},{")    

    print(jsonOutput)
    # return(jsonOutput)

if __name__ == '__main__':
   
    try:   
        start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')    #The 0th arg is the module filename.
        end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
    
    except:
        end_date = date.today()
        start_date = end_date-timedelta(days=7)
        
    try:
        utc = sys.argv[3]
    except:
        utc = 'no'    
         
    
    run_query(start_date,end_date,utc) 