#!/usr/bin/env python3
"""Test script for integration with Javascript and NodeJS.

Usage:

    python3 script.py <date>
"""
import sys

def main (startDate, endDate):

    print(startDate+" my "+endDate)
    
    sys.stdout.flush()
    







if __name__ == '__main__':
    
    try:
        
        startDate = sys.argv[1]
        endDate = sys.argv[2]
        
        
        main(startDate,endDate)
        
    except:
        
        startDate = "Hello World "
        endDate = "This is my script"
        main(startDate,endDate)
        
        