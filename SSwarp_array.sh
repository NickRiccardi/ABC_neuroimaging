#!/bin/sh
### name your job
#SBATCH --job-name=SSwarp_array
### specify number of cores to use (@SSwarper takes a long time to run, more cores will finish faster)
#SBATCH -n 14
#SBATCH -N 1
### %a specifies that the output file for each subject will be named according to their array ID
#SBATCH --output SSwarp_%a.out
#SBATCH --error SSwarp_%a.err
### list the subjects that you want to submit in this array
#SBATCH --array=1032,1036,1027,1029,1030,1048,1049,1050,1051,1052,1053,1054,1055,1056
### which partition do you want to use?
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm

### enters each subject directory according to their array ID (i.e. '1032', '1036', etc.)
cd ${SLURM_ARRAY_TASK_ID}
### runs SSwarper and places output files within the subject directory
@SSwarper T1.nii $SLURM_ARRAY_TASK_ID -giant_move -deoblique
