#!/bin/sh
### set job name
#SBATCH --job-name=WAV
### set number of cores to use
#SBATCH -n 14
#SBATCH -N 1
### output files named after array ID
#SBATCH --output proc.WAV_%a.out
#SBATCH --error proc.WAV_%a.err
### set array of subjects
#SBATCH --array=1006-1050
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm
module load python2.7/anaconda/5.0.0

### run the proc scripts for each subject specified in the array
tcsh -xef proc.ABC_${SLURM_ARRAY_TASK_ID} |& tee output.proc.ABC_${SLURM_ARRAY_TASK_ID}
