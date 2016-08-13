#!/usr/bin/env python
import sys

datefile = open("./stockprice/"+sys.argv[1]+"temp.txt")
#There are two colume in temp.txt DATE and Price
writefile = open(sys.argv[1]+".txt", 'wr')
        
line = datefile.readline()
line = line.split("\t")
#print line 
""" 
if str(line[0]) == sys.argv[1] + "0102":        
    print 'yes'
else:
    print 'no'    
"""
print line
temp = line
line = datefile.readline()
line = line.split("\t")
print line
for MON in range(1, 13):
    if MON == 1:
        DATE = 31
        Mon='01'
    if MON == 2:
        if int(sys.argv[1]) % 4 == 0:
            DATE = 29
            Mon='02'
        else:
            DATE = 28
            Mon='02' 
    if MON == 3:
        DATE = 31        
        Mon='03' 
    if MON == 4:
        DATE = 30
        Mon='04' 
    if MON == 5:
        DATE = 31
        Mon='05' 
    if MON == 6:
        DATE = 30
        Mon='06' 
    if MON == 7:
        DATE = 31
        Mon='07' 
    if MON == 8:
        DATE = 31
        Mon='08' 
    if MON == 9:
        DATE = 30
        Mon='09' 
    if MON == 10:
        DATE = 31
        Mon='10' 
    if MON == 11:
        DATE = 30
        Mon='11' 
    if MON == 12:
        DATE = 31
        Mon='12' 

    #temp = line
    #print temp[0]
    #print temp[1]

    for day in range(1, DATE+1):
        #print sys.argv[1] + "01" + str(JAN) 
        if day < 10:
            if str(line[0]) == sys.argv[1] + Mon + "0" + str(day):        
                writefile.write(str(line[0]) + "\t" + str(line[1].strip()) + "\n")
                temp = line
                line = datefile.readline()
                line = line.split("\t")
                print day
            else:
                if day < 10:
                    writefile.write(sys.argv[1] + Mon + "0" + str(day) + "\t" + str(temp[1].strip()) + "\n")    
                else:    
                    writefile.write(sys.argv[1] + Mon + str(day) + "\t" + str(temp[1].strip()) + "\n")    
        else:
            if str(line[0]) == sys.argv[1] + Mon + str(day):        
                writefile.write(str(line[0]) + "\t" + str(line[1].strip()) + "\n")
                temp = line
                line = datefile.readline()
                line = line.split("\t")
                print day
            else:
                if day < 10:
                    writefile.write(sys.argv[1] + Mon + "0" + str(day) + "\t" + str(temp[1].strip()) + "\n")    
                else:     
                    writefile.write(sys.argv[1] + Mon + str(day) +"\t" + str(temp[1].strip()) + "\n")    






datefile.close()
writefile.close() 

                   
