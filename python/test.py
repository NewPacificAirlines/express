#!/usr/bin/env python3
""" Test save pectab file.

Usage:

    python3 test.py <bagtagnumber> 
"""
import sys
import os


def saveFile(tagNumber):
    
    print('Tag number', tagNumber)

    tagNumberLong = '9808'+tagNumber

    filename = tagNumberLong+'.btp'
    print('filename ',filename)    
      
    path = '/log/'+filename  
      
    print('Current Working Directory ',os.getcwd())
    
    print('Path ',path)
                
    with open (path, 'w') as fp:
        pass
        fp.write('BTP123501')

if __name__ == '__main__':
       
    try:
        tagNumber = sys.argv[1]       #Tag number
        
        saveFile(tagNumber)
        
    except:
        
        print('error no tag number!')
        
