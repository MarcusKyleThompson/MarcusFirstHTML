# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:10:16 2020

@author: Marcus
"""


#FlightDataAnalyzer.py

data = open("flightdata.txt").read().splitlines()


dataTitles = data[0].split('<')

for x in dataTitles:
    print(x)

print(dataTitles[1])

