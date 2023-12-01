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


def run_query(start_date,end_date):   
    
    jsonList = []
    
    WhizTicketNumber = []
    ACH_Billed = []
    Address = []
    AgentEmpNumber = []
    AgentTill = []
    Authorization_Code = []
    Authorize_Response_BLOB = []
    Authorize_ResponseCode = []
    Authorize_ResponseText = []
    Authorized = []
    AuthorizeTransactionNumber = []
    BillingAddress = []
    BillingAddressDiff = []
    BillingCity = []
    BillingCountry = []
    BillingFax = []
    BillingPhone = []
    BillingState = []
    BillingZip = []
    Card_Code = []
    Card_Number = []
    CardPresent = []
    CashTotal = []
    CC_ExpirationDATE = []
    CheckTotal = []
    City = []
    Company = []
    Country = []
    CreditCardTotal = []
    CreditCardType = []
    Cust_ID = []
    Customer_TaxID = []
    Date_GP_Integrated = []
    Date_Issued = []
    Description_Invoice = []
    Detail_Charges = []
    Email_Address = []
    EraChargeTotal = []
    ExciseTax_Amount = []
    First_Name = []
    Gateway = []
    GPAccountID = []
    History = []
    Issued_By = []
    Last_Name = []
    ModifedDTS = []
    Non_UniqueVoucher = []
    OtherBillingInfo = []
    Payment_Type = []
    PaymentDetailLONGTEXT = []
    Phone = []
    RefID = []
    RefID_DATE = []
    RefundApproved = []
    RefundApprovedAgent = []
    RefundApprovedDATE = []
    RefundedAmount = []
    RefundProcessed = []
    RefundProcessedAgent = []
    RefundProcessedDATE = []
    RefundProcessingFee = []
    RefundReason = []
    RefundRequested = []
    RefundRequestedAgent = []
    RefundRequestedDATE = []
    RefundResearched = []
    RefundResearchedAgent = []
    RefundResearchedDATE = []
    Remarks = []
    SendCustomer_Email = []
    State = []
    Station = []
    Status = []
    Subtotal_Amount = []
    SyncRecordNumber = []
    SyncUUID = []
    TimeIssued = []
    Total_Amount = []
    Type = []
    UniqueVoucher = []
    Voided = []
    VoidedAgent = []
    VoidedDATE = []
    VoidedReason = []
    Zip = []
     
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
        
        sql = """SELECT * FROM WhizTicket WHERE (Date_Issued BETWEEN %s AND %s) 
        """
        
        cursor.execute(sql, params)
        records = cursor.fetchall()
        
        for row in records:
            try:
                WhizTicketNumber.append(str(row['WhizTicketNumber']))
            except:
                WhizTicketNumber.append('')       
                
        print(WhizTicketNumber)     
            
    except:
    
        print('error')
    
if __name__ == '__main__':
    
   
 
  
    try:    
        end_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
    except:
        end_date = date.today()
        
    try:   
        start_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')    #The 0th arg is the module filename.
    except:
        start_date = end_date-timedelta(days=1)
    
  

    print(start_date)
    print(end_date) 
    
    run_query(start_date,end_date) 
