#!/bin/sh
### set job name
#SBATCH --job-name=freesurfer_array
### set number of nodes (more is better for FreeSurfer)
#SBATCH -n 12
#SBATCH -N 1
### output files named after array ID
#SBATCH --output FS_%a.out
#SBATCH --error FS_%a.err
### set subjects that you want to run
#SBATCH --array=1001-1056
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm
module load freesurfer/2020-beta

### cd into each subject's data directory
cd ${SLURM_ARRAY_TASK_ID}
### create surfaces and put output in subject's data directory
### openmp number should match the number of nodes requested above
recon-all -s ${SLURM_ARRAY_TASK_ID}_FS -i T1.nii -sd /home/riccardn/data/ABC/${SLURM_ARRAY_TASK_ID} -all -parallel -openmp 12
