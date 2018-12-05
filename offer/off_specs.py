m= 'mandatory'
o='optional'
headerspec=[ #HEADER
[m,['RH']],
    [m,['trans_purpose','BIA','00',2,1]],
    [m,['request_id','BIA','00',30,3]],
    [m,['response_generation_date','BIA','00',6,4]],
    [m,['response_generation_time','BIA','00',8,5]],
[m,['HT'],],
    [m,['process_date','DTM','009',14,7,0,8]],
    [m,['process_time','DTM','009',14,7,8,14]],
    [o,['pipeline_name','N1','SJ',35,2]],
    [m,['pipeline_code','N1','SJ',17,4]],
[m,['\nRD']],
    [m,['dataset_request','LIN','',30,3]],
    [m,['reference_number','REF','',2,1]],
    [m,['data_available_code','REF','',30,2]],
    ]
O1 = [
        ['Un_line','NTE','ACC',1,60,2],
        [' '*238],
    ['\nO2'],
        ['Trans_purpose','BQT','',1,2,1],
        ['opav_posting_number','BQT','',2,45,2],
        ['opav_trans_dt','BQT','',3,6,3],
        ['DOC-ID','BQT','',6,2,6],
        ['oa_ft_ind','REF','TG',1,30,2],
        ['op_ac_tm_zone','DTM','145',1,30,6],
    ['\nO3'],
    ['\nO4'],
]
