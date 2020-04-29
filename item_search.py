# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:55:21 2020

@author: Nick
"""

import pandas as pd

#create subject list
subj_list = ['1011','1012','1014','1015','1016','1018','1019','1020','1021',
             '1022','1023','1024','1025','1026','1027','1028','1029','1030',
             '1032','1034','1035','1036','1037','1038','1039','1040','1041',
             '1042','1044','1045','1046','1047']

stim_subj = pd.DataFrame(columns = ['word'])

"""
- specify an item that you would like to search for
- refer to /ABC_neuroimaging/stimuli_and_design/master_word/ for item list
"""
stimsearch = ['work']
stim_df = {stim: pd.DataFrame() for stim in stimsearch}


#read in the subject data
for subj in subj_list:
    subj_filter = pd.read_csv('fMRI_fam-' + subj + '-1-Export.txt', encoding = 'utf-16', sep = '\t', header = 0)
    subj_name = str(subj)
    
#define subject start time
    start_time = subj_filter.iloc[1,12]

#merge useful columns for words and pics
    subj_filter['onset_times'] = subj_filter['famPresent.OnsetTime'].fillna(subj_filter['famPresentPic.OnsetTime'])
    subj_filter['onset_times'] = (subj_filter['onset_times'] - start_time)/1000
    subj_filter = subj_filter[pd.notnull(subj_filter['onset_times'])]
    subj_filter = subj_filter[['word','onset_times']]

#create master df of all words and their onset times for every subject
    stim_subj = pd.merge(stim_subj,subj_filter,on='word',how='outer')
    stim_subj = stim_subj.rename(columns={'onset_times':subj_name})

#output timing file csv for specified item, keeping participant #
for stim in stimsearch:
    item_df = stim_subj.loc[stim_subj['word'].isin(stimsearch)]
    item_df = item_df.dropna(axis=1,how='any')
    item_df.to_csv(stim + '_onset.txt', index=False, sep = ' ')
    