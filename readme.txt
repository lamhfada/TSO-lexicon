DATA��m

corpus��b/tmp2/cylai/DATA/TARFILE

�b/tmp2/cylai/DATA/News_index�̦�index�n��

code����b/tmp2/cylai/code



Text data������

��RUN"CombinXML"��corpus�̭�XML����r�����X�ӡA�u���@�ӿ�Jinput�ΨӽT�{�n�������@�~�A�A�ӥ�lemur�i��index�AIndex�����ڬO�bMAC�W���Ϊ��A�]��MAC��lemur INDEX���|�Ӥ���ƦC�C

Index���H��A"dumpindex il"���@��txt�ɡA�M���read_index.pyŪ��pkl��




stock price data������

RUN"ParsePrice.sh"��ѻ���z�X�ӡA�����input�A�Ĥ@�ӬO���q�A�ĤG�ӬO�~���C



Correlation


Run"CalUcor.py"�p��r�P�ѻ��������סA���T�ӿ�J�Ĥ@�ӬO���q�A�ĤG�ӬO�~���A�ĤT�ӬO���~index��unit term(dumpindex s)�A��X�����G���O���g�LDTW�ACor�������O�������r�Atop�Ocorrelation�j��0.8���r�Ahtop�Ocorrelation�j��0.5���r�C


��z��SVM�榡

�n�]���e�n��index�n3�~���r�٦�4�~���r�A�٦��p��ncorrelation��word list(��~)�A���]�ntrain 2000-2001 test 2002����N�n��1999-2002�A�٦�2000-2002�~��index�A�H��2000-2001�~��high correlation word list�C

��������run "readDFOtherWord0.py" �O��z�X���Ftopword�H�~��L�r��DF���O0����ơA��8��input�A�Ĥ@�ӬO4�~���~���A�ĤG�ӬO�T�~���A�ĤT�ӬO���q�W�١A�ĥ|�ӬO�s���i�H�H�K���A�ĪZ�ӬO��~word list���~���A�Ĥ��ӬOunit term���ƶq�A�ĤC�ӬO4�~���Ĥ@�~�Ѽ�+1�A�ĤK�ӬO4�~�� 2 3�~���ѼơC���]�ntrain 2000-2001 test 2002�~�A���N�O
./readDFOtherWord0.py 1999-2002 2000-2002 apple 1 2000-2001 377097 366 730  

run "readUDFoneday.py" �O�]�����r����weight���Ainput��W���@�ˡC



