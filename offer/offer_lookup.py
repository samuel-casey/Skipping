def make_table(edi):
    delimiters = ['|','~','-', '*']
    edi = edi.splitlines()
    delim_count = [edi[1].count(delim) for delim in delimiters]
    delim = delimiters[delim_count.index(max(delim_count))]
    print('Delimiter is ',delim,[line for line in zip(delimiters,delim_count)])
    edi = [line.split(delim) for line in edi]
    newseg, newedi =[],[]
    for line in edi:
        if line[0] in ['ST']:
            newedi.append(newseg)
            newseg = []
        newseg.append(line)
    return newedi
    
def find_value(spec, listy):
    def header_lookup(spec, listy):
        if len(spec[1])==1:
            value = spec[1][0]
            return value
        elem,code,length,pos = spec[1][1], spec[1][2], spec[1][3], spec[1][4]
        value = [line[pos] for line in listy if line[0]==elem and line[1]==code]
        print(value)
        if len(value)>1:
            print('MULTIPLE VALUES HELPPPP')
        else:
            try:
                value = value[0]
            except:
                value =''
        if len(spec[1])>5 and value!='':
            value = value[spec[5]:spec[6]]
        if length>len(value):
            value = value+' '*(length-len(value))
        return value 
   
    if listy[0][1] == '846':
        return header_lookup(spec, listy)



edi = '''ISA~00~          ~00~          ~01~808300594      ~12~6112240022     ~180821~0919~U~00304~000000001~0~P~>
GS~IB~OFFER~6112240022~180821~0919~1~X~003040
ST~846~0001
BIA~00~S8~CN187016~180821~081912
DTM~009~~~~~DTS~20180821081912
N1~SJ~~1~116025180
N1~41~~1~883328874
LIN~1~OA~1
REF~IX~Y
CTT~1
SE~9~0001
GE~1~1
GS~IB~OFFER~6112240022~180821~0919~2~X~003040
ST~840~1
BQT~00~083354~180821~~~CR~03
REF~H5~RR~864
REF~CP~Y
REF~QU~N
REF~PH~HR
REF~ZZ~NONE
REF~A1~PT~NTE
REF~H6~Y
DTM~098~~~~~RTS~20180821080810-20180821100000
DTM~102~~~NO~~DTS~20180821080810
DTM~103~~~~~DTS~20180821110000
DTM~334~~~~~DTS~20180821113000
DTM~580~~~~~RD8~20180822-20180822
LIN~~RN~2~SH~1~SV~2~MO~FT
PID~S~~AP~~NA~~~Y
PID~F~~AP~~NA~~~N
N1~SJ~~1~116025180
N1~SE~~1~006976666
PER~IC~MARC CUTHBERTSON~TE~7168577228~FX~7168577823
PO1~1~~~~~AM~1~BT~3~F5~MO~R9~2~MO~FT~RA~N
REF~99~A
REF~SV~1
SAC~C~~AP~RES~~~~1.302~~~~~RATE
SAC~A~~AP~RES~~~~4.1743~~~~~RATE
SDQ~BZ~~MO~4500~MQ~4500
N1~M2~MILLENNIUM - HOLDING POINT (LN-1/31~29~1389428
QTY~12~0
N1~MQ~NATL FUEL - (NIPS)~29~158447
QTY~12~4500
N1~M2~TITLE TRANSFER POINT - NORTH~29~251064
QTY~12~4500
N1~MQ~TITLE TRANSFER POINT - NORTH~29~251064
QTY~12~0
CTT~1
SE~36~1
GE~1~2
GS~IB~OFFER~6112240022~180821~0919~3~X~003040
ST~864~1
BMG~00~083354~RC
DTM~145~~~~~DTS~20180821080810
N1~SJ~~1~116025180
MIT~ZZZ~1
MSG~recall and reput for any reason
SE~7~1
ST~864~2
BMG~00~083354~RC
DTM~145~~~~~DTS~20180821080810
N1~SJ~~1~116025180
MIT~REV~1
MSG~ROLLOVER TERMS: YR-TO-YR
SE~7~2
GE~2~3
IEA~3~000000001
'''