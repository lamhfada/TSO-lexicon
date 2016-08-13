#!/usr/bin/env python
import sys

Stockprice = open('./stockprice/'+sys.argv[1]+sys.argv[2]+'.txt', 'rb')

temp = open('./stockprice/'+sys.argv[1]+sys.argv[2]+'.txt', 'rb')

price = []
for l in Stockprice:
    price.append(l.strip())
    break

for u in temp:
    price.append(u.strip())

save = open('./RafN/'+sys.argv[1]+sys.argv[2]+'RaF.txt', 'wb')

RaF = []
rise = 0
fall = 0
ne = 0


print len(price)
for x in range(0, len(price)-1):
    
    if float(price[x+1]) - float(price[x]) == 0:
        RaF.append(1)
        save.write('1\n')
        #fall = fall + 1
    elif (float(price[x+1]) - float(price[x])) / float(price[x]) > 0.008:
        RaF.append(2)
        save.write('2\n')
    elif (float(price[x+1]) - float(price[x])) / float(price[x]) < -0.008:   
        RaF.append(0)
        save.write('0\n')
    else:
        save.write('1\n')
save.close()

#print rise
#print fall
#print ne
