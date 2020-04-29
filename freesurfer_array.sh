#!/bin/sh
#SBATCH --job-name=freesurfer_array
#SBATCH -n 12
#SBATCH -N 1
#SBATCH --output FS_%a.out
#SBATCH --error FS_%a.err
#SBATCH --array=1001-1056
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm
module load freesurfer/2020-beta

cd ${SLURM_ARRAY_TASK_ID}
recon-all -s ${SLURM_ARRAY_TASK_ID}_FS -i T1.nii -sd /home/riccardn/data/ABC/${SLURM_ARRAY_TASK_ID} -all -parallel -openmp 12
