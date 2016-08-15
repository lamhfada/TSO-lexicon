#!/bin/bash

#mkdir ${1}

cat ../DATA/Stockprice/${1}Price.txt | grep ^$2 -B1 | awk '{print $1 "\t" $2}' > ./stockprice/${2}temp.txt



./date.py $2

mv ${2}.txt ./stockprice

rm ./stockprice/${2}temp.txt

cat ./stockprice/${2}.txt | awk '{print $2}' > ./stockprice/${1}${2}.txt

rm ./stockprice/${2}.txt





