#!/usr/bin/env python3
"""Send file to PECTAB based printer


Usage:

    createBTPFile.py parameters
    
"""
import sys
import re
import time
from find_Printer import find_printer as find_printer
from send_BTP import send_Pectab_file as send_file

def createBTPFile(printer,legs,company,tagNumber,recordLoc,flightDate,lastName,firstName,fullDest,fullState,flight1,dest1,flight2,dest2,dest2Dep,flight3,dest3,dest3Dep,flight4,dest4,dest4Dep,selectee,returnData,rush):
    
    try:
        # print('Printer ',printer)
        
        if returnData != '1':
        
            address = find_printer(printer)
            
            print('printer_IP', address)
        
    except:
        
        print('error occured find_printer')
        
    try:

        
        # print(tagNumber)
        # print('Legs ',legs)
        # print('Tag Number',tagNumberLong)
        
        # print(recordLoc)
        # print(flightDate)
        # print(lastName)
        # print(firstName)
        # print(fullDest)
        # print(fullState)
        # print(flight1)
        # print(dest1)
        # print(flight2)
        # print(dest2)
        # print(dest2Dep)
        # print(flight3)
        # print(dest3)
        # print(dest3Dep)
        
        s = tagNumber
        # print('original tag ',tagNumber)
        suffix = " ".join(re.split("[^a-zA-Z]*", tagNumber)).strip()
        
        # print('suffix of tagnumber ',suffix)
        # print('length ', len(suffix))
        
        tagNumber = "".join(c for c in s if  c.isdecimal())
        tagBanner = ""
        
        if rush == '1':
            tagNumberLong = '2808'+tagNumber
            tagNumberCode = '28087H'+tagNumber
            tagBanner = 'RUSH BAGS'
        else:
            tagNumberLong = '9808'+tagNumber
            tagNumberCode = '98087H'+tagNumber
                  
            if suffix == 'E':
                tagBanner = 'VOL SEP'
            elif suffix == 'N':
                tagBanner = 'NON REV'
            
        filename = tagNumberLong+'.btp'
        
        t1 = tagNumber[0:2]
        t2 = tagNumber[2:4]
        t3 = tagNumber[4:6]
       
        tagNumber = '7H '+t1+'-'+t2+'-'+t3
        
        # print(tagNumber)
        
        print('filename ',filename)    
        
        # print('Current Working Directory ',os.getcwd())
        
        
        path = './log/'+filename
                    
        print('Path ', path)
                    
        with open (path, 'w') as fp:
            pass
            fp.write('BTP123501')
            
            # print('tagBanner ',tagBanner)

            
            
                
                    
            if legs == '1':
                # print('1 segment tag')
                fp.write('#15'+tagBanner)
                fp.write('#29'+flight1)
                fp.write('#32'+dest1)
                fp.write('#36'+tagNumber)
                fp.write('#38'+tagNumberLong)
                fp.write('#60'+tagNumberCode)
                fp.write('#70'+company)
                fp.write('#82'+fullDest)
                fp.write('#83'+fullState)
                fp.write('#84'+lastName+'/')
                fp.write('#85'+firstName)
                fp.write('#86'+recordLoc)
                fp.write('#87'+flightDate)
                fp.write('#\f')
                
            elif legs == '2':
        
                # print('2 segments tag')
                fp.write('#15'+tagBanner)
                fp.write('#25'+flight1)
                fp.write('#26'+'DEP '+dest2Dep)
                fp.write('#27'+dest1)
                fp.write('#29'+flight2)
                fp.write('#32'+dest2)
                fp.write('#36'+tagNumber)
                fp.write('#38'+tagNumberLong)
                fp.write('#60'+tagNumberCode)
                fp.write('#70'+company)
                fp.write('#82'+fullDest)
                fp.write('#83'+fullState)
                fp.write('#84'+lastName+'/')
                fp.write('#85'+firstName)
                fp.write('#86'+recordLoc)
                fp.write('#87'+flightDate)
                fp.write('#\f')
                
            elif legs == '3':
        
                # print('3 segments tag')
                fp.write('#15'+tagBanner)
                fp.write('#20'+flight1)
                fp.write('#21'+'DEP '+dest2Dep)
                fp.write('#22'+dest1)
                fp.write('#25'+flight2)
                fp.write('#26'+'DEP '+dest3Dep)
                fp.write('#27'+dest2)
                fp.write('#29'+flight3)
                fp.write('#32'+dest3)
                fp.write('#36'+tagNumber)
                fp.write('#38'+tagNumberLong)
                fp.write('#60'+tagNumberCode)
                fp.write('#70'+company)
                fp.write('#82'+fullDest)
                fp.write('#83'+fullState)
                fp.write('#84'+lastName+'/')
                fp.write('#85'+firstName)
                fp.write('#86'+recordLoc)
                fp.write('#87'+flightDate)
                fp.write('#\f')
                
            elif legs == '4':
        
                # print('4 segments tag')
                fp.write('#15'+tagBanner)
                fp.write('#16'+flight1)
                fp.write('#17'+'DEP '+dest2Dep)
                fp.write('#18'+dest1)
                fp.write('#20'+flight2)
                fp.write('#21'+'DEP '+dest3Dep)
                fp.write('#22'+dest2)
                fp.write('#25'+flight3)
                fp.write('#26'+'DEP '+dest4Dep)
                fp.write('#27'+dest3)
                fp.write('#29'+flight4)
                fp.write('#32'+dest4)
                fp.write('#36'+tagNumber)
                fp.write('#38'+tagNumberLong)
                fp.write('#60'+tagNumberCode)
                fp.write('#70'+company)
                fp.write('#82'+fullDest)
                fp.write('#83'+fullState)
                fp.write('#84'+lastName+'/')
                fp.write('#85'+firstName)
                fp.write('#86'+recordLoc)
                fp.write('#87'+flightDate)
                fp.write('#\f')
                
            else:
                # print('any other number of segments tag')
                fp.write('#15'+tagBanner)
                fp.write('#29'+flight1)
                fp.write('#32'+dest1)
                fp.write('#36'+tagNumber)
                fp.write('#38'+tagNumberLong)
                fp.write('#60'+tagNumberCode)
                fp.write('#70'+company)
                fp.write('#82'+fullDest)
                fp.write('#83'+fullState)
                fp.write('#84'+lastName+'/')
                fp.write('#85'+firstName)
                fp.write('#86'+recordLoc)
                fp.write('#87'+flightDate)
                fp.write('#\f')
            
        # print(path)
        
        if returnData != '1':

            if selectee == '1':
                send_file('python/pectabs/common_data_pectab_4_selectee.btt',address)
            else:
                send_file('python/pectabs/common_data_pectab_4.btt',address)
            
            time.sleep(3) # Sleep for 3 seconds
            
            send_file(path,address)
            
        else:
            
            data = open(path)
            
            print(data.read())
        
        
        
    except:

        print('Error creating Pectab File Occured')  

if __name__ == '__main__':
       
    try:
        printer = sys.argv[1]       #Printer name 
        legs = sys.argv[2]
        company = sys.argv[3]
        tagNumber = sys.argv[4]    
        recordLoc = sys.argv[5]
        flightDate = sys.argv[6]
        lastName = sys.argv[7]
        firstName = sys.argv[8]
        fullDest = sys.argv[9]
        fullState = sys.argv[10]
        flight1 = sys.argv[11]
        dest1 = sys.argv[12]
        flight2 = sys.argv[13]
        dest2 = sys.argv[14]
        dest2Dep = sys.argv[15]
        flight3 = sys.argv[16]
        dest3 = sys.argv[17]
        dest3Dep = sys.argv[18]
        flight4 = sys.argv[19]
        dest4 = sys.argv[20]
        dest4Dep = sys.argv[21]

        selectee = sys.argv[22]
        
        returnData = sys.argv[23]
        rush = sys.argv[24]
        
        # print(printer)
        # print(tagNumber)
        
        createBTPFile(printer,legs,company,tagNumber,recordLoc,flightDate,lastName,firstName,fullDest,fullState,flight1,dest1,flight2,dest2,dest2Dep,flight3,dest3,dest3Dep,flight4,dest4,dest4Dep,selectee,returnData,rush)

        
    except:
        
        print("No target or parameters entered")         
    