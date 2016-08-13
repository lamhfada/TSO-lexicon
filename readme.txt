DATA位置

corpus放在/tmp2/cylai/DATA/TARFILE

在/tmp2/cylai/DATA/News_index裡有index好的

code都放在/tmp2/cylai/code



Text data的部分

先RUN"CombinXML"把corpus裡面XML的文字分離出來，只有一個輸入input用來確認要分離哪一年，再來用lemur進行index，Index部分我是在MAC上面用的，因為MAC的lemur INDEX完會照日期排列。

Index完以後，"dumpindex il"成一個txt檔，然後用read_index.py讀成pkl檔




stock price data的部分

RUN"ParsePrice.sh"把股價整理出來，有兩個input，第一個是公司，第二個是年分。



Correlation


Run"CalUcor.py"計算字與股價的相關度，有三個輸入第一個是公司，第二個是年分，第三個是那年index的unit term(dumpindex s)，輸出的結果都是有經過DTW，Cor結尾的是全部的字，top是correlation大於0.8的字，htop是correlation大於0.5的字。


整理成SVM格式

要跑之前要先index好3年的字還有4年的字，還有計算好correlation的word list(兩年)，假設要train 2000-2001 test 2002那麼就要有1999-2002，還有2000-2002年的index，以及2000-2001年的high correlation word list。

都有之後run "readDFOtherWord0.py" 是整理出除了topword以外其他字的DF都是0的資料，有8個input，第一個是4年的年份，第二個是三年的，第三個是公司名稱，第四個是編號可以隨便給，第武個是兩年word list的年份，第六個是unit term的數量，第七個是4年的第一年天數+1，第八個是4年中 2 3年的天數。假設要train 2000-2001 test 2002年，那就是
./readDFOtherWord0.py 1999-2002 2000-2002 apple 1 2000-2001 377097 366 730  

run "readUDFoneday.py" 是跑全部字都有weight的，input跟上面一樣。



