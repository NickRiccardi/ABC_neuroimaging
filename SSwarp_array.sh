#!/bin/sh
#SBATCH --job-name=SSwarp_array
#SBATCH -n 14
#SBATCH -N 1
#SBATCH --output SSwarp_%a.out
#SBATCH --error SSwarp_%a.err
#SBATCH --array=1032,1036,1027,1029,1030,1048,1049,1050,1051,1052,1053,1054,1055,1056
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm

cd ${SLURM_ARRAY_TASK_ID}
@SSwarper T1.nii $SLURM_ARRAY_TASK_ID -giant_move -deoblique
