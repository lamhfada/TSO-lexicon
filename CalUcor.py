#!/usr/bin/env python
import sys
import math
import cPickle as pickle
import mlpy
import numpy as np
from pymur import *
from scipy.stats.stats import pearsonr
from operator import itemgetter, attrgetter
#if len(sys.argv) == 0:
#    print 'first is company second is year'
#    sys.exit()

i = Index("../DATA/News_index/"+sys.argv[2])

StockIndex = []
StockFile = open('./stockprice/'+sys.argv[1]+sys.argv[2]+'.txt')
for l in StockFile:
    StockIndex.append(float(l.strip()))



#Uterm = 291770

Uterm = int(sys.argv[3]) 
'''
SPnum = []
for y in StockIndex:
    SPnum.append(float(y))
if sys.argv[2] == '2000':
    Uterm = 212714
if sys.argv[2] == '2001':
    Uterm = 202619
if sys.argv[2] == '2002':
    Uterm = 211797
if sys.argv[2] == '2003':
    Uterm = 209751
if sys.argv[2] == '2004':
    Uterm = 200128
if sys.argv[2] == '2005':
    Uterm = 204263
if sys.argv[2] == '2006':
    Uterm = 209339
if int(sys.argv[2]) % 4 ==0:
    YEAR = 366
else:
    YEAR = 365
'''
YEAR = int(sys.argv[4])   
#print len(doc)
pkl_file = open('../DATA/News_index/'+sys.argv[2]+'.pkl', 'rb')
words = pickle.load(pkl_file)
pkl_file.close()
#print len(doc2)
writeCor = open("./DCor/"+sys.argv[1]+"/N"+sys.argv[1]+sys.argv[2]+"Cor.txt", 'wr') 
writetop = open("./DCor/"+sys.argv[1]+"/N"+sys.argv[1]+sys.argv[2]+"top.txt",'wr')
writehtop = open('./DCor/'+sys.argv[1]+'/N'+sys.argv[1]+sys.argv[2]+'htop.txt', 'wr')
#f = open("Pcorrelation.txt", 'wr')
Cor =[]
Test = []

for term_id in range(1, Uterm+1):
    tfIndoc = []
    term = i.term(term_id)
    wordTF = []    
    for x in range(1, YEAR+1):
         try:
             wordTF.append(words[term][2][x])
         except:
            wordTF.append(0)
    
    wordTFArray = np.array(wordTF)
    indexArray = np.array(StockIndex)
    dist, cost, path = mlpy.dtw_std(wordTFArray, indexArray, dist_only=False)
    
    #f.write(term+" "+" ".join(map(lambda x: str(x), pearsonr(tmpD, SPnum))))
    #f.write("\n")    
    Cor.append([term, pearsonr(wordTFArray[path[0]], indexArray[path[1]])[0],pearsonr(wordTFArray[path[0]],indexArray[path[1]])[1]]) 
    print Uterm


Test = sorted(Cor, key=lambda co : co[1], reverse=True)
#Test = sorted(Cor, key=lambda Co : Co[0])
#print Uterm
for u in range(0, len(Test)):
    writeCor.write(str(Test[u][0])+'\t'+str(Test[u][1])+"\n")
for top in range(0, len(Test)):
    if Test[top][1] > 0.8:   
        writetop.write(str(Test[top][0])+'\t'+str(Test[top][1])+"\n")
for top in range(0, len(Test)):
    if Test[top][1] > 0.5:   
        writehtop.write(str(Test[top][0])+"\n")
    
#print Test[u]
    #if len(tmpD) != 366:
    #    ErNum +=1
    #    ErList.append(term)
writeCor.close()
writetop.close()
writehtop.close()
        #print(tfIndoc)
#print ErNum
#print ErList
#print doc[3]
#print doc2[team]
#print doc
#print doc[3]

"""
#for doc_id in range(1, len(i)+1):
    doc = i.document(doc_id)
    docLen = len(doc)
    terms = dict(zip (set(doc), map (doc.count, set(doc))))
    features = []
    #features.append[terms[0]]    
#print(terms)
"""    


#print doc[0].count
