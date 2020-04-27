# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 15:08:25 2020

@author: Nick
"""

import pandas as pd

#list subjects
subj_list = ['1011','1012','1014','1015','1016','1018','1019','1020','1021',
             '1022','1023','1024','1025','1026','1027','1028','1029','1030',
             '1032','1034','1035','1036','1037','1038','1039','1040','1041',
             '1042','1044','1045','1046','1047']

"""
- specify continous amiplitude modulation variable of interest (e.g. Freq, Conc.M, AoA, etc.)
- refer to /ABC_neuroimaging/stimuli_and_design/master_word/ for other codes
"""
AM_var = 'Freq'

#read in master word list file found in refer to /ABC_neuroimaging/stimuli_and_design/master_word/
master_word = pd.read_csv('masterword_clean.csv', header=0)
master_word = master_word[['word',AM_var]]

"""
- define the codes that we want to use for different conditions
- refer to /ABC_neuroimaging/stimuli_and_design/master_word/ for other codes
- add whichever conditions you are interested in by creating a list of the codes
"""

words_Code1 = list(range(1,10))
words_Code1.extend(list(range(12,51)))
nonwords_Code1 = list(range(51,54))
conc_Code1 = [1,2,3,13,18,19,20,27,28,34,35,42,43,44]
abstract_Code1 = [7,8,9,12,16,17,24,25,26,31,32,39,40,41,48,49,50]
highFreq_Code1 = [1,4,7,12,14,16,18,21,24,27,29,31,34,36,39,42,45,48]
lowFreq_Code1 = [3,6,9,20,23,26,38,41,44,47,50]

"""
- dictionary of our condition names and corresponding code lists
- add or remove conditions from this dictionary as you see fit
"""

cond_dict = {'words':words_Code1, 'conc':conc_Code1, 
             'abstract':abstract_Code1, 'highFreq':highFreq_Code1, 'lowFreq':lowFreq_Code1}

#read in the subject data
for subj in subj_list:
    subj_filter = pd.read_csv('fMRI_fam-' + subj + '-1-Export.txt', encoding = 'utf-16', sep = '\t', header = 0)

#define scanner start time
    start_time = subj_filter.iloc[1,12]
    
#merge and create useful columns for words and pics (e.g. onset times, response times, etc.)
    subj_filter['onset_times'] = subj_filter['famPresent.OnsetTime'].fillna(subj_filter['famPresentPic.OnsetTime'])
    subj_filter['RTTimes'] = subj_filter['famPresent.RTTime'].fillna(subj_filter['famPresentPic.RTTime'])
    subj_filter['Acc'] = subj_filter['famPresent.ACC'].fillna(subj_filter['famPresentPic.ACC'])
    subj_filter['RT'] = subj_filter['famPresent.RT'].fillna(subj_filter['famPresentPic.RT'])
    subj_filter['Response'] = subj_filter['famPresent.RESP'].fillna(subj_filter['famPresentPic.RESP'])

#obtain true onset and RTs for timing file       
    subj_filter['onset_times'] = (subj_filter['onset_times'] - start_time)/1000
    subj_filter['RTTimes'] = (subj_filter['RTTimes'] - start_time)/1000
    
#merge the subject df with the master word list, aligning the AM_var with each item    
    subj_filter = pd.merge(subj_filter,master_word, on='word', how='left')   
    subj_filter = subj_filter[pd.notnull(subj_filter[AM_var])]
    subj_filter = subj_filter.round(2)
    
#create RT timing files
    RTTimes = subj_filter[['RTTimes']]
    RTTimes = RTTimes[RTTimes > 0].T.dropna(axis=1)
    RTTimes.to_csv(subj + '_RTTimes.txt', index=False, sep = ' ', header=None)

#create 'married' onset timing files for each condition    
    for cond in cond_dict:
        cond_filter = subj_filter[subj_filter['Code1'].isin(cond_dict[cond])]
        cond_filter['AM_marry'] = cond_filter['onset_times'].astype(str) + '*' + cond_filter[AM_var].astype(str)
        cond_onset = cond_filter[['AM_marry']].T
        cond_onset.to_csv(subj + '_' + AM_var + '_' + cond + '_onset_' +'.txt', index=False, sep = ' ', header=None)
    
    
