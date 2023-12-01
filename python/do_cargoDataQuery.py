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


def run_query(start_date, end_date, origin, dest):    
    
    jsonList = []
    
    Accounting_Info = []
    Agent_Fees = []
    AgentEmpNumber = []
    AgentIATACode = []
    AirwayBill_Num = []
    AlsoNote_Address = []
    AlsoNote_CityStateZip = []
    AlsoNote_First_Name = []
    AlsoNote_Last_Name = []
    AlsoNote_Phone = []
    AlternateAWB = []
    Authorized = []
    Brief_Remarks = []
    CharterID = []
    Consignee_Address = []
    Consignee_First_Name = []
    Consignee_ID = []
    Consignee_Last_Name = []
    Consignee_Phone = []
    ConsigneeCity = []
    ConsigneeState = []
    ConsigneeZip = []
    Date_Modified = []
    Date_Paid = []
    Date_Received = []
    DeclaredValue = []
    FirstCarrierDestination = []
    FirstCarrierName = []
    FirstCarrierOrigin = []
    FlatRateItem = []
    FlatRateTotal = []
    Freight_ID = []
    Freight_Type = []
    From_Location = []
    Full_From = []
    Full_T = []
    GPAccountID = []
    Hazmat_items = []
    Insurance = []
    InterMed_Car_Address = []
    InterMed_Car_CityStateZip = []
    InterMed_Car_Phone = []
    InterMed_Car_Waybill = []
    Intermediate_Carrier_Name = []
    Inventory_Description = []
    MustRead = []
    Non_UniqueVoucher = []
    NonChargeableWeight = []
    NonTaxable = []
    PaidBy = []
    Payment_ID = []
    Payment_Type = []
    Piece_Count = []
    Prepaid_Amount = []
    PrepaidWeightCharge = []
    Printed = []
    Priority_and_Oversized_Frt = []
    Priority_or_Oversized_Frt = []
    Rate = []
    RateOveride = []
    RecvAgent = []
    Remarks = []
    ScheduledDate = []
    ScheduledDate2 = []
    ScheduledDate3 = []
    ScheduledFlight = []
    ScheduledFlight2 = []
    ScheduledFlight3 = []
    SecondCarrierDestination = []
    SecondCarrierName = []
    Shipped_All = []
    Shipped_Partial = []
    Shipper_Address = []
    Shipper_City = []
    Shipper_First_Name = []
    Shipper_ID = []
    Shipper_Last_Name = []
    Shipper_Phone = []
    Shipper_PO_GBL_TR = []
    Shippers_Fees = []
    ShipperState = []
    ShipperZip = []
    Station = []
    SubTotal = []
    SyncUUID = []
    Tax = []
    Time_Modified = []
    Time_Received = []
    To_Location = []
    Total_Cost = []
    Total_Weight = []
    UniqueVoucher = []
    ValCharge = []
    Voided = []

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                            port=3306,
                                            database='skedflex',
                                            user='stats',
                                            password='WetSampleBridge22$',
                                            auth_plugin='mysql_native_password',
                                            use_pure=True)
        cursor = connection.cursor(dictionary=True)
        
        params = (start_date,end_date)
        
        sql = """SELECT * FROM Freight_Current WHERE (Date_Received BETWEEN %s AND %s) 
        """
        
        if origin != '':
            
            if(origin != ''):
                origin_sql = ''
            
            origin_list = origin.split(",")    
            origin_sql += " AND ("
            # print(tails_list)
            
            for i in origin_list:
                origin_sql += " From_Location LIKE '%"+i+"%' OR "
                
            origin_sql = origin_sql[:-4]
            origin_sql += ") " 
            sql += origin_sql
            
            
            
        if dest != '':
            
            if(dest != ''):
                dest_sql = ''
            
            dest_list = dest.split(",")    
            dest_sql += " AND ("
            # print(tails_list)
            
            for i in dest_list:
                dest_sql += " To_Location LIKE '%"+i+"%' OR "
                
            dest_sql = dest_sql[:-4]
            dest_sql += ") " 
            sql += dest_sql
            
            
            
        # print(sql)
        # print(params)
              
        cursor.execute(sql, params)
        records = cursor.fetchall()
        
        for row in records:
            
            try:                
                stringData = row['Accounting_Info']
                stringData = stringData.decode('string_escape')
                Accounting_Info.append(stringData)
            except:
                Accounting_Info.append('')
                
            try:
                Agent_Fees.append(str(row['Agent_Fees']))
            except:
                Agent_Fees.append('')

            try:
                AgentEmpNumber.append(row['AgentEmpNumber'])
            except:
                AgentEmpNumber.append('')

            try:
                AgentIATACode.append(row['AgentIATACode'])
            except:
                AgentIATACode.append('')

            try:
                AirwayBill_Num.append(str(row['AirwayBill_Num']))
            except:
                AirwayBill_Num.append('')

            try:
                AlsoNote_Address.append(row['AlsoNote_Address'])
            except:
                AlsoNote_Address.append('')

            try:
                AlsoNote_CityStateZip.append(row['AlsoNote_CityStateZip'])
            except:
                AlsoNote_CityStateZip.append('')

            try:
                AlsoNote_First_Name.append(row['AlsoNote_First_Name'])
            except:
                AlsoNote_First_Name.append('')

            try:
                AlsoNote_Last_Name.append(row['AlsoNote_Last_Name'])
            except:
                AlsoNote_Last_Name.append('')

            try:
                AlsoNote_Phone.append(row['AlsoNote_Phone'])
            except:
                AlsoNote_Phone.append('')

            try:
                AlternateAWB.append(row['AlternateAWB'])
            except:
                AlternateAWB.append('')

            try:
                if row['Authorized'] == 1 :
                    Authorized.append('Yes')
                else:
                    Authorized.append('No')
            except:
                Authorized.append('No')

            try:
                stringData = row['Brief_Remarks']
                stringData = stringData.decode('string_escape')
                Brief_Remarks.append(stringData)
            
            except:
                Brief_Remarks.append('')

            try:
                CharterID.append(str(row['CharterID']))
            except:
                CharterID.append('')

            try:
                Consignee_Address.append(row['Consignee_Address'])
            except:
                Consignee_Address.append('')

            try:
                Consignee_First_Name.append(row['Consignee_First_Name'])
            except:
                Consignee_First_Name.append('')

            try:
                Consignee_ID.append(str(row['Consignee_ID']))
            except:
                Consignee_ID.append('')

            try:
                stringData = row['Consignee_Last_Name']
                stringData = stringData.decode('string_escape')
                Consignee_Last_Name.append(stringData)
            except:
                Consignee_Last_Name.append('')

            try:
                Consignee_Phone.append(row['Consignee_Phone'])
            except:
                Consignee_Phone.append('')

            try:
                ConsigneeCity.append(row['ConsigneeCity'])
            except:
                ConsigneeCity.append('')

            try:
                ConsigneeState.append(row['ConsigneeState'])
            except:
                ConsigneeState.append('')

            try:
                ConsigneeZip.append(row['ConsigneeZip'])
            except:
                ConsigneeZip.append('')

            try:                
                dateField = row['Date_Modified']
                date_time = dateField.strftime("%m/%d/%Y")
                Date_Modified.append(date_time)  
            except:
                Date_Modified.append('')

            try:
                dateField = row['Date_Paid']
                date_time = dateField.strftime("%m/%d/%Y")
                Date_Paid.append(date_time)  
            except:
                Date_Paid.append('')

            try:
                dateField = row['Date_Received']
                date_time = dateField.strftime("%m/%d/%Y")
                Date_Received.append(date_time)  
            except:
                Date_Received.append('')

            try:
                DeclaredValue.append(str(row['DeclaredValue']))
            except:
                DeclaredValue.append('')

            try:
                FirstCarrierDestination.append(row['FirstCarrierDestination'])
            except:
                FirstCarrierDestination.append('')

            try:
                FirstCarrierName.append(row['FirstCarrierName'])
            except:
                FirstCarrierName.append('')

            try:
                FirstCarrierOrigin.append(row['FirstCarrierOrigin'])
            except:
                FirstCarrierOrigin.append('')

            try:
                FlatRateItem.append(str(row['FlatRateItem']))
            except:
                FlatRateItem.append('')

            try:
                FlatRateTotal.append(str(row['FlatRateTotal']))
            except:
                FlatRateTotal.append('')

            try:
                Freight_ID.append(str(row['Freight_ID']))
            except:
                Freight_ID.append('')

            try:
                Freight_Type.append(row['Freight_Type'])
            except:
                Freight_Type.append('')

            try:
                From_Location.append(row['From_Location'])
            except:
                From_Location.append('')

            try:
                stringData = row['Full_From']
                stringData = stringData.decode('string_escape')
                Full_From.append(stringData)
            except:
                Full_From.append('')

            try:
                Full_T.append(row['Full_T'])
            except:
                Full_T.append('')

            try:
                GPAccountID.append(row['GPAccountID'])
            except:
                GPAccountID.append('')

            try:
                Hazmat_items.append(str(row['Hazmat_items']))
            except:
                Hazmat_items.append('')

            try:
                Insurance.append(str(row['Insurance']))
            except:
                Insurance.append('')

            try:
                InterMed_Car_Address.append(row['InterMed_Car_Address'])
            except:
                InterMed_Car_Address.append('')

            try:
                InterMed_Car_CityStateZip.append(row['InterMed_Car_CityStateZip'])
            except:
                InterMed_Car_CityStateZip.append('')

            try:
                InterMed_Car_Phone.append(str(row['InterMed_Car_Phone']))
            except:
                InterMed_Car_Phone.append('')

            try:
                InterMed_Car_Waybill.append(row['InterMed_Car_Waybill'])
            except:
                InterMed_Car_Waybill.append('')

            try:
                Intermediate_Carrier_Name.append(row['Intermediate_Carrier_Name'])
            except:
                Intermediate_Carrier_Name.append('')

            try:
                Inventory_Description.append(row['Inventory_Description'])
            except:
                Inventory_Description.append('')

            try:
                MustRead.append(str(row['MustRead']))
            except:
                MustRead.append('')

            try:
                Non_UniqueVoucher.append(row['Non_UniqueVoucher'])
            except:
                Non_UniqueVoucher.append('')

            try:
                NonChargeableWeight.append(str(row['NonChargeableWeight']))
            except:
                NonChargeableWeight.append('')

            try:
                NonTaxable.append(str(row['NonTaxable']))
            except:
                NonTaxable.append('')

            # try:
            #     OtherCharges.append(json.dumps(row['OtherCharges']), separators= (',', ':'))
            # except:
            #     OtherCharges.append('')

            try:
                PaidBy.append(row['PaidBy'])
            except:
                PaidBy.append('')

            try:
                Payment_ID.append(str(row['Payment_ID']))
            except:
                Payment_ID.append('')

            try:
                Payment_Type.append(row['Payment_Type'])
            except:
                Payment_Type.append('')

            try:
                Piece_Count.append(str(row['Piece_Count']))
            except:
                Piece_Count.append('')

            try:
                Prepaid_Amount.append(str(row['Prepaid_Amount']))
            except:
                Prepaid_Amount.append('')

            try:
                PrepaidWeightCharge.append(str(row['PrepaidWeightCharge']))
            except:
                PrepaidWeightCharge.append('')

            try:
                Printed.append(str(row['Printed']))
            except:
                Printed.append('')

            try:
                Priority_and_Oversized_Frt.append(str(row['Priority_and_Oversized_Frt']))
            except:
                Priority_and_Oversized_Frt.append('')

            try:
                Priority_or_Oversized_Frt.append(str(row['Priority_or_Oversized_Frt']))
            except:
                Priority_or_Oversized_Frt.append('')

            try:
                Rate.append(str(row['Rate']))
            except:
                Rate.append('')

            try:
                RateOveride.append(str(row['RateOveride']))
            except:
                RateOveride.append('')

            try:
                RecvAgent.append(row['RecvAgent'])
            except:
                RecvAgent.append('')

            try:
                stringData = row['Remarks']
                stringData = stringData.decode('string_escape')
                Remarks.append(stringData)
            except:
                Remarks.append('')

            try:
                dateField = row['ScheduledDate']
                date_time = dateField.strftime("%m/%d/%Y")
                ScheduledDate.append(date_time)  
            except:
                ScheduledDate.append('')

            try:
                dateField = row['ScheduledDate2']
                date_time = dateField.strftime("%m/%d/%Y")
                ScheduledDate2.append(date_time)  
            except:
                ScheduledDate2.append('')

            try:
                dateField = row['ScheduledDate3']
                date_time = dateField.strftime("%m/%d/%Y")
                ScheduledDate3.append(date_time)  
            except:
                ScheduledDate3.append('')

            try:
                ScheduledFlight.append(str(row['ScheduledFlight']))
            except:
                ScheduledFlight.append('')

            try:
                ScheduledFlight2.append(str(row['ScheduledFlight2']))
            except:
                ScheduledFlight2.append('')

            try:
                ScheduledFlight3.append(str(row['ScheduledFlight3']))
            except:
                ScheduledFlight3.append('')

            try:
                SecondCarrierDestination.append(row['SecondCarrierDestination'])
            except:
                SecondCarrierDestination.append('')

            try:
                SecondCarrierName.append(row['SecondCarrierName'])
            except:
                SecondCarrierName.append('')

            try:
                Shipped_All.append(str(row['Shipped_All']))
            except:
                Shipped_All.append('')

            try:
                Shipped_Partial.append(str(row['Shipped_Partial']))
            except:
                Shipped_Partial.append('')

            try:
                Shipper_Address.append(row['Shipper_Address'])
            except:
                Shipper_Address.append('')

            try:
                Shipper_City.append(row['Shipper_City'])
            except:
                Shipper_City.append('')

            try:
                Shipper_First_Name.append(row['Shipper_First_Name'])
            except:
                Shipper_First_Name.append('')

            try:
                Shipper_ID.append(str(row['Shipper_ID']))
            except:
                Shipper_ID.append('')

            try:
                Shipper_Last_Name.append(row['Shipper_Last_Name'])
            except:
                Shipper_Last_Name.append('')

            try:
                Shipper_Phone.append(row['Shipper_Phone'])
            except:
                Shipper_Phone.append('')

            try:
                Shipper_PO_GBL_TR.append(row['Shipper_PO_GBL_TR'])
            except:
                Shipper_PO_GBL_TR.append('')

            try:
                Shippers_Fees.append(str(row['Shippers_Fees']))
            except:
                Shippers_Fees.append('')

            try:
                ShipperState.append(row['ShipperState'])
            except:
                ShipperState.append('')

            try:
                ShipperZip.append(row['ShipperZip'])
            except:
                ShipperZip.append('')

            try:
                Station.append(row['Station'])
            except:
                Station.append('')

            try:
                SubTotal.append("{:,.2f}".format(row['SubTotal']))
            except:
                SubTotal.append('')


            try:
                SyncUUID.append(row['SyncUUID'])
            except:
                SyncUUID.append('')

            try:
                Tax.append("{:,.2f}".format(row['Tax']))
            except:
                Tax.append('')

            try:
                Time_Modified.append(datetime.strftime(dateutil.parser.parse(row['Time_Modified']),'%H:%M:%S'))
            except:
                Time_Modified.append('')

            try:
                Time_Received.append(datetime.strftime(dateutil.parser.parse(row['Time_Modified']),'%H:%M:%S'))

            except:
                Time_Received.append('')

            try:
                To_Location.append(row['To_Location'])
            except:
                To_Location.append('')

            try:
                Total_Cost.append("{:,.2f}".format(row['Total_Cost']))
            except:
                Total_Cost.append('0.00')

            try:                
                Total_Weight.append(str(int(row['Total_Weight'])))
            except:
                Total_Weight.append('')

            try:
                stringData = row['UniqueVoucher']
                stringData = stringData.decode('string_escape')
                UniqueVoucher.append(stringData)
            except:
                UniqueVoucher.append('')

            try:
                ValCharge.append(str(row['ValCharge']))
            except:
                ValCharge.append('')

            try:
                if row['Voided'] == 1:
                    Voided.append('Yes')
                else:
                    Voided.append('No')
            except:
                Voided.append('No')


        
    except mysql.connector.Error as error:
        print("Failed to select from MySQL table {}".format(error))


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
  
    
    index = 0
    # print(len(records))
    while index < len(Accounting_Info):
        
        # jsonLine = ''
        
        jsonLine='{"Accounting_Info":"'+Accounting_Info[index]+'","AgentEmpNumber":"'+AgentEmpNumber[index]+'","Agent_Fees":"'+Agent_Fees[index]+'","AgentIATACode":"'+AgentIATACode[index]+\
            '","AirwayBill_Num":"'+AirwayBill_Num[index]+'","AlsoNote_Address":"'+AlsoNote_Address[index]+'","AlsoNote_CityStateZip":"'+AlsoNote_CityStateZip[index]+\
            '","AlsoNote_First_Name":"'+AlsoNote_First_Name[index]+'","AlsoNote_Last_Name":"'+AlsoNote_Last_Name[index]+'","AlsoNote_Phone":"'+AlsoNote_Phone[index]+\
            '","AlternateAWB":"'+AlternateAWB[index]+'","Authorized":"'+Authorized[index]+'","Brief_Remarks":"'+Brief_Remarks[index]+'","CharterID":"'+CharterID[index]+\
            '","Consignee_Address":"'+Consignee_Address[index]+'","Consignee_First_Name":"'+Consignee_First_Name[index]+'","Consignee_ID":"'+Consignee_ID[index]+\
            '","Consignee_Last_Name":"'+Consignee_Last_Name[index]+'","Consignee_Phone":"'+Consignee_Phone[index]+'","ConsigneeCity":"'+ConsigneeCity[index]+\
            '","ConsigneeState":"'+ConsigneeState[index]+'","ConsigneeZip":"'+ConsigneeZip[index]+'","Date_Modified":"'+Date_Modified[index]+\
            '","Date_Paid":"'+Date_Paid[index]+'","Date_Received":"'+Date_Received[index]+'","DeclaredValue":"'+DeclaredValue[index]+\
            '","FirstCarrierDestination":"'+FirstCarrierDestination[index]+'","FirstCarrierName":"'+FirstCarrierName[index]+\
            '","FirstCarrierOrigin":"'+FirstCarrierOrigin[index]+'","FlatRateItem":"'+FlatRateItem[index]+'","FlatRateTotal":"'+FlatRateTotal[index]+\
            '","Freight_ID":"'+Freight_ID[index]+'","Freight_Type":"'+Freight_Type[index]+'","From_Location":"'+From_Location[index]+\
            '","Full_From":"'+Full_From[index]+'","Full_T":"'+Full_T[index]+'","GPAccountID":"'+GPAccountID[index]+'","Hazmat_items":"'+Hazmat_items[index]+\
            '","Insurance":"'+Insurance[index]+'","InterMed_Car_Address":"'+InterMed_Car_Address[index]+\
            '","InterMed_Car_CityStateZip":"'+InterMed_Car_CityStateZip[index]+'","InterMed_Car_Phone":"'+InterMed_Car_Phone[index]+\
            '","InterMed_Car_Waybill":"'+InterMed_Car_Waybill[index]+'","Intermediate_Carrier_Name":"'+Intermediate_Carrier_Name[index]+\
            '","Inventory_Description":"'+Inventory_Description[index]+'","MustRead":"'+MustRead[index]+'","Non_UniqueVoucher":"'+Non_UniqueVoucher[index]+\
            '","NonChargeableWeight":"'+NonChargeableWeight[index]+'","NonTaxable":"'+NonTaxable[index]+\
            '","PaidBy":"'+PaidBy[index]+'","Payment_ID":"'+Payment_ID[index]+'","Payment_Type":"'+Payment_Type[index]+'","Piece_Count":"'+Piece_Count[index]+\
            '","Prepaid_Amount":"'+Prepaid_Amount[index]+'","PrepaidWeightCharge":"'+PrepaidWeightCharge[index]+'","Printed":"'+Printed[index]+\
            '","Priority_and_Oversized_Frt":"'+Priority_and_Oversized_Frt[index]+'","Priority_or_Oversized_Frt":"'+Priority_or_Oversized_Frt[index]+\
            '","Rate":"'+Rate[index]+'","RateOveride":"'+RateOveride[index]+'","RecvAgent":"'+RecvAgent[index]+'","Remarks":"'+Remarks[index]+\
            '","ScheduledDate":"'+ScheduledDate[index]+'","ScheduledDate2":"'+ScheduledDate2[index]+'","ScheduledDate3":"'+ScheduledDate3[index]+\
            '","ScheduledFlight":"'+ScheduledFlight[index]+'","ScheduledFlight2":"'+ScheduledFlight2[index]+'","ScheduledFlight3":"'+ScheduledFlight3[index]+\
            '","SecondCarrierDestination":"'+SecondCarrierDestination[index]+'","SecondCarrierName":"'+SecondCarrierName[index]+'","Shipped_All":"'+Shipped_All[index]+\
            '","Shipped_Partial":"'+Shipped_Partial[index]+'","Shipper_Address":"'+Shipper_Address[index]+'","Shipper_City":"'+Shipper_City[index]+\
            '","Shipper_First_Name":"'+Shipper_First_Name[index]+'","Shipper_ID":"'+Shipper_ID[index]+'","Shipper_Last_Name":"'+Shipper_Last_Name[index]+\
            '","Shipper_Phone":"'+Shipper_Phone[index]+'","Shipper_PO_GBL_TR":"'+Shipper_PO_GBL_TR[index]+'","Shippers_Fees":"'+Shippers_Fees[index]+\
            '","ShipperState":"'+ShipperState[index]+'","ShipperZip":"'+ShipperZip[index]+'","Station":"'+Station[index]+'","SubTotal":"'+SubTotal[index]+\
            '","SyncUUID":"'+SyncUUID[index]+'","Tax":"'+Tax[index]+'","Time_Modified":"'+Time_Modified[index]+'","Time_Received":"'+Time_Received[index]+\
            '","To_Location":"'+To_Location[index]+'","Total_Cost":"'+Total_Cost[index]+'","Total_Weight":"'+Total_Weight[index]+\
            '","UniqueVoucher":"'+UniqueVoucher[index]+'","ValCharge":"'+ValCharge[index]+'","Voided":"'+Voided[index]+'"}'
        
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
        end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
    except:
        end_date = date.today()
        
    try:   
        start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')    #The 0th arg is the module filename.
    except:
        start_date = end_date-timedelta(days=1)
    
    try:    
        origin = sys.argv[3]
    except:
        origin = ''
    
    try:        
        dest = sys.argv[4]
    except:
        dest = ''
        
        
    # print(start_date)
    # print(end_date)    
    # print(origin)
    # print(dest)    
       
    run_query(start_date,end_date,origin,dest) 

