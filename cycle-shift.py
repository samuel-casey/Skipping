import sys
# txt ='''
# 114754	201710012215	201710060000	2017	10		10/06/2017	0000		02085	HARBISON-WALKER REFRACTORIES - FULTON, MO	Market Zone	D	MQ	DPQ	BZ	N	1723	1723	2	1721	Panhandle Eastern Pipeline	45256641	MO	Callaway	2085	02085_20171006_ 45256641_D	FIN	
# 114754	201709162215	201709210000	2017	09		09/21/2017	0000		02085	HARBISON-WALKER REFRACTORIES - FULTON, MO	Market Zone	D	MQ	DPQ	BZ	N	1723	1723	1	1722	Panhandle Eastern Pipeline	45256641	MO	Callaway	2085	02085_20170921_ 45256641_D	FIN	
# 114753  201709012215    201709120000    2017    09              09/12/2017      0000            05586   GUARDIAN GLASS  Market Zone     D       MQ      DPQ     BZ      N       12000   12000   5250    6750    Panhandle Eastern Pipeline      45256641        MI      Monroe  5586    05586_20170912_ 45256641_D      FIN     
# 114753	201711162215	201711280000	2017	11		11/28/2017	0000		JACPL	JACKSON PIPELINE	Market Zone	D	MQ	DPQ	BZ	N	85100	85100	1	85099	Panhandle Eastern Pipeline	45256641	MI	Jackson		JACPL_20171128_ 45256641_D	FIN	
# '''

if len(sys.argv) > 1:
     txt = sys.argv[1]
else:
    print('Please enter file name as argument')
    exit()
with open(txt) as file:  
        txt = file.read()

txt = txt.splitlines()