# ABC fMRI

##Introduction

This is a series of EPrime (https://pstnet.com/products/e-prime/), Python, AFNI (https://afni.nimh.nih.gov/), FreeSurfer (https://surfer.nmr.mgh.harvard.edu/), and SLURM scripts built to streamline functional neuroimaging data analysis for the Aging Brain Cohort project at the University of South Carolina (ABC@UofSC) while leveraging the Hyperion supercomputing cluster. The current pipeline is designed specifically for the 'fMRI_fam' task which consists of single word presentations. However, in the future we will be adding scripts to generate word- or phrase-level timing files for the 'fMRI_passage' task, consisting of stories and passages presented auditorily to participants. There are many experimental questions that one can ask while analyzing these tasks due to a wide range of continuous and categorical variables of interest. Here, we have created a pipeline for analysis of major contrasts (e.g. words vs. nonwords, pictures vs. words, foreign language passages vs. English passages), and we have provided notes throughout the scripts advising users on how the pipeline may be modified to suit their more specific experimental questions.

##Recommended Software

Python 2.7 or later
AFNI_20.1.02 or later
FreeSurfer v6.0.0, or Freesurfer/2020-beta module if using the Hyperion Cluster
Access to Hyperion supercomputing cluster

