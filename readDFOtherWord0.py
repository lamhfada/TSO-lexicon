#!/usr/bin/env python
import sys
import math
import cPickle as pickle
import numpy as np
from pymur import *
from scipy.stats.stats import pearsonr
from operator import itemgetter, attrgetter
i = Index("../DATA/News_index/"+sys.argv[1])
i2 = Index("../DATA/News_index/"+sys.argv[2])

wordlist = open('DCor/'+sys.argv[3]+'/N'+sys.argv[3]+sys.argv[5]+'htop.txt')
Raf = open('./RafN/'+sys.argv[3]+sys.argv[2]+'RaF.txt')

RF = []
timesword = {}
for te in wordlist:
    timesword[te.strip()] = 1

for ll in Raf:
    RF.append(ll.strip())
FYEAR = int(sys.argv[7])
F3YEAR = int(sys.argv[7]) + int(sys.argv[8])

wordArray =[]

#time = float(sys.argv[3])

for l in wordlist:
    wordArray.append(l.strip())
print len(wordArray)
UDF_train = open('UDF/'+sys.argv[3]+sys.argv[2]+'UDF_train_other0_'+sys.argv[4]+'.txt', 'wb')
UDF_test = open('UDF/'+sys.argv[3]+sys.argv[2]+'UDF_test_other0_'+sys.argv[4]+'.txt', 'wb')
Uterm = int(sys.argv[6]) 
YEAR = 1461   
#print len(doc)
pkl_file = open('../DATA/News_index/'+sys.argv[1]+'.pkl', 'rb')
words = pickle.load(pkl_file)
pkl_file.close()
for u in range(FYEAR, F3YEAR):
    UDF_train.write(str(RF[u-FYEAR])+' ')
    wordDF = []
    for term_id in range(0, Uterm+1):
        
        term = i2.term(term_id)

        try:
            timesword[term]
            time = float(sys.argv[4])
        except:
            time = float(0)
        try:
            T2 = float(words[term][2][u-1])
        except:
            T2 = float(0)
        try:
            T1 = float(words[term][2][u])
        except:
            T1 = float(0)
        Difference = T2 - T1
        wordDF.append(Difference*time)
    print len(wordDF)
    for x in range(0, Uterm):    
        index = x + 1
        if wordDF[x] == 0:
            continue
        UDF_train.write(str(index) + ':' + str(wordDF[x]) + ' ')
    UDF_train.write('\n')


for u in range(F3YEAR, 1462):
    UDF_test.write(str(RF[u-FYEAR])+' ')
    wordDF = []
         
    for term_id in range(0, Uterm+1):
            
        term = i2.term(term_id)
        try:
            timesword[term]
            time = float(sys.argv[4])
        except:
            time = float(0)
        try:
            T2 = float(words[term][2][u-1])
        except:
            T2 = float(0)
        try:
            T1 = float(words[term][2][u])
        except:
            T1 = float(0)
        Difference = T2 - T1
        wordDF.append(Difference*time)
    print len(wordDF)
    for x in range(0, Uterm):    
        index = x + 1
        if wordDF[x] == 0:
            continue
        UDF_test.write(str(index) + ':' + str(wordDF[x]) + ' ')
    UDF_test.write('\n') 


#print doc[0].count
