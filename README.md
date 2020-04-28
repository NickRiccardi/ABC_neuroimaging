# ABC fMRI

## Introduction

This is a series of EPrime (https://pstnet.com/products/e-prime/), Python, AFNI (https://afni.nimh.nih.gov/), FreeSurfer (https://surfer.nmr.mgh.harvard.edu/), and SLURM scripts built to streamline functional neuroimaging data analysis for the Aging Brain Cohort project at the University of South Carolina (ABC@UofSC) while leveraging the Hyperion supercomputing cluster. The current pipeline is designed specifically for the reading ('fMRI_fam') task which consists of single word presentations. However, in the future we will be adding scripts to generate word- or phrase-level timing files for the listening ('passage_fMRI') task, consisting of stories and passages presented auditorily to participants. There are many experimental questions that one can ask while analyzing these tasks due to a wide range of continuous and categorical variables of interest. Here, we have created a pipeline for analysis of major contrasts (e.g. words vs. nonwords, pictures vs. words, foreign language passages vs. English passages), and we have provided notes advising users on how the pipeline may be modified to suit their more specific experimental questions.

## Recommended Software

Python 2.7 or later, with Pandas 1.0.3 or later

AFNI_20.1.02 or later

netpbm packages: pnmcat, pbmtext, pnmscale, pbmtopgm, (pnmcomp OR pamcomp)

FreeSurfer v6.0.0, or Freesurfer/2020-beta module if using the Hyperion Cluster

Access to Hyperion supercomputing cluster (optional but highly recommended)

## Stimuli and Design

For information about the stimuli, please see the 'stimuli_and_design' directory. Within this, there is a detailed README which describes the experimental design, stimuli, and provides examples of variables of interest that could be investigated. Also included in this directory are the EPrime scripts used for experimental presentation and .csv documents listing the stimuli and their associated psycholinguistic variables. Especially important is the 'master_word' directory, which provides the coding system that we have implemented for categorical variables of interest in the reading ('fMRI_fam') task. Understanding the coding system is vital for creating the fMRI timing files used by AFNI (Step #4 in the 'Pipeline Flow', described in sections below).

## Pipeline Flow

![flowchart](https://user-images.githubusercontent.com/64374486/80516712-de1cb100-8951-11ea-833e-30b9778cb6e4.png)

The figure above shows the order in which the pipeline should be executed. Steps #4 and greater will depend on the investigator's desired analysis, and those scripts will need to be edited in order to reflect the specific experimental question (more information on this is provided in subsequent sections).

## Steps and associated scripts

### Step #1: Subject-specific anatomical alignment to standardized space

#### SSwarp_array.sh

This is a SLURM batch array submission script calling AFNI's @SSwarper command, which 1) aligns each subject's anatomical T1 to a standard space target and 2) skull-strips that anatomical volume. This is AFNI's recommendation for 'pre-preprocessing' (https://www.biorxiv.org/content/10.1101/308643v1.full.pdf), and is vital for proper execution of Steps #5 and above of our pipeline (actual analysis of the fMRI data). The script enters each desired subject's data directory (named '1001', '1002', etc.) and applies @SSwarper to their anatomical scan (assumed to be named 'T1.nii'), warping it to the MNI152_2009_template_SSW.nii.gz template. 'giant_move' and 'deoblique' are specified here in case the subject's head was very tilted within the scanner.

Within each subject's directory, output files should include (where $ = the subject's number):
  - anatDO.$.nii
  - anatU.$.nii
  - anatUA.$.nii
  - anatUAC.$.nii
  - anatS.$.nii
  - anatSS.$.nii
  - anatQQ.$.nii
  - anatQQ.$.aff12.1D
  - anatQQ.$WARP.nii
  - anatQQ.$.nii
  - AM$.jpg
  - MA$.jpg
The .jpg files are used to visually inspect the success of @SSwarper, while anatQQ.$.nii, anatQQ.$.aff12.1D, and anatQQ.$WARP.nii are called in Steps #5 and above of the pipeline.

### Step #2: Create brain surfaces

#### freesurfer_array.sh

This is a SLURM batch array submission script calling FreeSurfer's 'recon-all' command (https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all), which performs all of FreeSurfer's standard cortical reconstruction process using a subject's anatomical scan (assumed to be named 'T1.nii'). The script enters each desired subject's data directory (named '1001', '1002', etc.), creates a new FS output directory (e.g. '1001_FS'), and places the output into that directory (example output files listed here: https://surfer.nmr.mgh.harvard.edu/fswiki/ReconAllOutputFiles). 'parallel' and 'openmp #' must be specified here in order to use multiple Hyperion cores. The # following openmp should match the number of cores you wish to use in the batch script.

### Step #3: Decide desired analysis

Here, one must determine what type of analysis they wish to conduct, including which categorical or continuous variables of interest they want to choose. The scripts in the following sections have been written using very broad contrasts (i.e. words vs. nonwords, words vs. pictures, or foreign language vs. English passages), but a large number of more specific analyses are possible using our multiple psycholinguistic variables and categorical coding system provided in /stimuli_and_design/master_word/.

### Step #4: Create timing files

The following Python scripts use EPrime's experimental output files for each subject (named 'fMRI_fam-$subjectnumber-1-Export.txt') to generate AFNI-formatted .txt timing files for response times and stimuli onset, which will be used in subsequent steps. The scripts should be executed in a single directory where every subject's EPrime output file is stored. One should modify the scripts to reflect their desired analysis.

#### timing.py

This script should be used if your desired analysis is purely categorical (i.e. no continuous psycholinguistic variables included). The current version creates separate timing .txt files for each subject for response times to all stimuli and onset times for the following categories: words, nonwords, pictures, concrete words, abstract words, high frequency words, and low frequency words. Categories can be added or deleted at the user's discretion.

#### AM_marry.py

This script should be used if your desired analysis contains continuous variables (e.g. Age of acquisition, semantic diversity, etc.) for the purpose of 'marrying' stimuli onset times with the continuous variable associated with each specific stimulus. The current version, for each subject, marries our continous 'Freq' (word frequency) variable to the onset times for following categories: all words, concrete words, abstract words, high frequency words, and low frequency words. Output is .txt timing files that can be used with AFNI's amplitude modulation regression (https://afni.nimh.nih.gov/pub/dist/doc/misc/Decon/AMregression.pdf), which is AFNI's method of finding voxels whose activation is modulated by continuous variables. For example, using amplitude modulation and AM_marry.py for the all word category and frequency variable, you could find voxels that 1) are activated by words, regardless of frequency and 2) are modulated by the continuous frequency variable.

#### item_search.py

This script will be used for item-wise analysis, wherein an activation map will be created for each item, averaging across all of the subjects who saw that specific item. The current version creates a Pandas Dataframe where the rows are every stimulus seen by every participant thus far, and the columns represent each individual subject. The cells show the onset times at which the subjects saw a specific stimulus. Also included is the ability to search for a specific stimulus by its name, outputting a .csv file that contains the onset times for that single item, getting rid of all the subjects who did not see that item.

### Step #5: Modify the cmd.* scripts as desired

Note: If using the cluster, you do not actually run these scripts. Step #6 will call these scripts as needed.

These scripts assume that Steps #1 and #4 have been successfully completed. Within each subject's directory should be the .txt timing files, the output of @SSwarper, and 'fMRI_fam.nii' and 'fMRI_passage.nii'. The template MNI152_2009_template_SSW.nii.gz should be saved in a master directory with its path specified within the cmd.* scripts (via 'set tpath').

Two sample cmd.* scripts are provided:
 - cmd.ap.ABC_fam_make_proc
 - cmd.ap.ABC_pass_make_proc

These are scripts that will be used to generate AFNI's proc analysis scripts (Step #6), with the 'fam' version being built for the reading task and the 'pass' version for the listening task. For the reading task, built-in contrasts include words vs. nonwords and words vs. pictures, while the listening task only contains foreign language vs. English passages. These scripts were closely based on AFNI's current analysis recommendations (https://www.biorxiv.org/content/10.1101/308643v1.full.pdf). Users should feel free to modify these scripts as they see fit, and will need to modify their scripts based on the contrasts that they have chosen for their analysis.

### Step #6: Generate ANFI proc scripts

#### make_proc.sh

This is a batch submission script which will run the cmd.* scripts from Step #5, generating AFNI proc scripts for every subject listed within the cmd.* scripts. Example output can be found in **proc.ABC_1006.

### Step #7: Run the analysis

#### famWAV_array.sh
#### pass_array.sh

This step contains two scripts, depending on if the investigator is analyzing data from the reading (famWAV_array.sh) or listening (pass_array.sh) task. These are batch array submission scripts which will run all of the proc scripts for each subject that were generated in Step #6. Separate results directories will be generated for each subject in the master directory.
