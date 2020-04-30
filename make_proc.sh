#!/bin/sh
### set job name
#SBATCH --job-name=make_proc
### request number of nodes (should always be 1 for this script)
#SBATCH -n 1
#SBATCH -N 1
#SBATCH --output make_proc.out
#SBATCH --error make_proc.err
#SBATCH -p soph

#source /share/apps/Modules/3.2.10/init/modules.sh
module load afni
module load netpbm
module load python2.7/anaconda/5.0.0

### generate AFNI proc script for every subject specified within these cmd.* scripts
### comment out *fam or *pass if you're only focusing on one of the tasks
tcsh cmd.ap.ABC_fam_make_proc
tcsh cmd.ap.ABC_pass_make_proc
