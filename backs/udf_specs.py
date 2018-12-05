### Header, element, code,  length, relative position (minus 1), 
### (OPTIONAL: Concat pos start, and concat pos end, and another optional of if 
###  it is a reverse lookup (such as in LIN))
import csv
udf=[ #HEADER
    ['RH'],
    ['trans_purpose','BIA','00',2,1],
    ['request_id','BIA','00',30,3],
    ['response_generation_date','BIA','00',6,4],
    ['response_generation_time','BIA','00',8,5],
    ['HT'],
    ['process_date','DTM','009',14,7,0,8], 
    ['process_time','DTM','009',14,7,8,14],
    ['pipeline_name','N1','SJ',35,4],
    ['pipeline_code','N1','SJ',17,4],
    ['\nRD'],
    ['dataset_request','LIN','',30,3],
    ['reference_number','REF','',2,1],
    ['data_available_code','REF','',30,2],
    ### END OF HEADER
    ### AWARD
    ['\nH1'],
        ['aw_set_purpose','BQR','',2,1],
        ['aw_offer_number','BQR','',45,2],
        ['aw_bid_number','REF','BD',30,2],
    	['reference_number','REF','H5',30,2],
        [' '*15],
        [' '*2], 
        ['transaction_date','DTM','009',35,7],
        ['request_id','BIA','',30,3],
        [' '*15],
        ['re_releasable_ind','REF','H6',1,2],
        ['award_number','REF','IF',30,2],	
    ['\nN1'],
        ['special_terms_text','NTE','GEN',350,2],
    ['\nN2'],
        ['qty_text_description', 'NTE', 'QUT', 350,2],
    ['\nN3'],
        ['recall_terms','NTE', 'ZZZ', 350, 2],
    ['\nH2'],
        ['aw_tm_zone','DTM','050',2,4],
        ['capacity_aw_dt','DTM','050',14,7,0,8],
        ['capacity_aw_tm','DTM','050',14,7,8,14],
        ['aw_post_dt','DTM','103',14,7,0,8],
        ['aw_post_tm','DTM','103',14,7,8,14],
        ['aw_beg_dt','DTM','580',35,7,0,8],
        ['aw_beg_tm','DTM','580',35,7,8,14],
        ['aw_end_dt','DTM','580',35,7,15,23],
        ['aw_end_tm','DTM','580',35,7,23,29],
    ['\nH3'],
        ['aw_pad_ind','LIN','SH',30,0,0],
        ['aw_prev_rel_ind','LIN','RN',30,0,0],
        ['aw_perm_rel_ind','LIN','SV',30,7,0],
        ['aw_rt_sched','LIN','MO',30,9,1],
        ['aw_entity_legal_name','N1','SJ',35,2],
        ['aw_entity_duns_id','N1','SJ',2,3],
        ['aw_pl_code','N1','SJ',17,4],
        ['aw_pad_bidder_pl_affil','N1','SJ',2,5],
        ['aw_rel_entity2_legal_name','N1','SE',35,2],
        ['aw_rel_entity2_duns_ind','N1','SE',2,3],
        ['aw_rel_entity2_code_number','N1','SE',17,4],
        ['aw_entity2_legal_name','N1','BY',35,2],
        ['aw_entity2_duns_ind','N1','BY',2,3],
        ['aw_entity2_code_number','N1','BY',17,4],
        ['aw_pad_bidder_rel_affil','N1','SE',2,5],
    
    ['\nOL'],
        ['aw_pkg_type_code','PO1','BT',30,'0',0],
        ['aw_rate_form_code','PO1','AM',30,'0',0],
        ['aw_rate_unit_code','PO1','F5',30,0,0],
        [' '*30],
        [' '*30],
        ['aw_pct_dollar_code','REF','99',30,2],
        [' '*9],
        [' '*9],
        [' '*9],
        ['','SDQ','',2],
        ['','SDQ','AQ',15,0,0],
        ['','SDQ','CV',15,7,0],
        [' '*9],
        [' '*9],
        [' '*9],
        ['','DTM','',8,7,{1:'448',6:'RD8'},0,8],
        ['aw_seasonal_end_dt','DTM','',8,7,{1:'448',6:'RD8'},9,17],
        ['','REF','SV',30,2],
    ['\nUL'],
        ['res_max_rate','SAC', '',9,8,{1:'A',4:'RES',13:'RATE'},0,0],
        ['res_max_award','SAC', '',9,8,{1:'R',4:'RES',13:'RATE'},0,0],
        ['res_max_rate','SAC', '',9,8,{1:'R',4:'RES',13:'PMAX'},0,0],
        ['res_max_rate','SAC', '',9,8,{1:'A',4:'VOL',13:'RATE'},0,0],
        ['res_max_rate','SAC', '',9,8,{1:'R',4:'VOL',13:'RATE'},0,0],
        ['res_max_rate','SAC', '',9,8,{1:'R',4:'VOL',13:'PMAX'},0,0],
        ['res_max_rate','SAC', '',9,8,{1:'C',4:'VOL',13:'CPCT'},0,0],
        ['res_max_rate','SAC', '',9,8,{1:'A',4:'DEM',13:'RATE'},0,0],
        ['s_chg_type','SAC', '',2,4,{1:'A',4:'DEM',13:'RATE'},0,0],
        ['','SAC', '',9,8,{1:'R',4:'DEM',13:'RATE'},0,0],
        ['','SAC', '',9,4,{1:'R',4:'DEM',13:'RATE'},0,0],
        ['','SAC', '',9,8,{1:'R',4:'DEM',13:'PMAX'},0,0],
        ['','SAC', '',9,4,{1:'R',4:'DEM',13:'PMAX'},0,0],
        ['s_chg_type(2)','SAC', '',2,4,{1:'R',4:'DEM',13:'PMAX'},0,0],
        # COMMENT : I AM TOO LAZY TO FILL OUT THE REST OF THE REDUNDANT UL LINE, BUT THE INFRASTRUCTURE IS HERE
    ['\nIL'],
        ['aw_gtp_type_code1','N1','',2,1,['G1','G2','IJ','M2','MQ','MV','S9',"SB",'WR'],0,0], # MAY BE A UDF CODE VIOLATION HERE
        ['gtp_lookup','N1','',35,2,['G1','G2','IJ','M2','MQ','MV','S9',"SB",'WR'],0,0],
        ['','N1','S9',17,4],
        [' '*17],
        

        
        
        
        
        
        
        


    # ['\nUL'],
    #     ['res_max_rate','SAC','A',9,8],
    # ['\nIL'],
]

# TO MAKE IT A CSV UNCOMMENT
# with open('csvfile.csv', "w") as output:
#     writer = csv.writer(output, lineterminator='\n')
#     for val in udf:
#         writer.writerow(val)   

udf_header = udf[:14]
udf_award = udf[14:]
udf_il =udf[92:]
print(udf_il)