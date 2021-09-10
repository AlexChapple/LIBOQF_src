#!/bin/bash -e
echo $SLURM_ARRAY_TASK_ID
DIRECTORY="Omega_10_tau_01_phi_pi"
cd /nesi/project/uoa03404/work/$DIRECTORY/data/$SLURM_ARRAY_TASK_ID
pwd

# Run the little boxes simulation
/nesi/project/uoa03404/work/$DIRECTORY/data/$SLURM_ARRAY_TASK_ID/LIBOQF

