#!/bin/sh
#SBATCH --job-name=WAV
#SBATCH -n 14
#SBATCH -N 1
#SBATCH --output proc.WAV_%a.out
#SBATCH --error proc.WAV_%a.err
#SBATCH --array=1006-1050
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm
module load python2.7/anaconda/5.0.0

tcsh -xef proc.ABC_${SLURM_ARRAY_TASK_ID} |& tee output.proc.ABC_${SLURM_ARRAY_TASK_ID}
