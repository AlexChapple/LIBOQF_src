#!/bin/bash -e
echo $SLURM_ARRAY_TASK_ID
DIRECTORY="tau08"
FILE_TO_RUN="LIBOQF_tau08"
cd /nesi/project/uoa03404/masters/tau/$DIRECTORY/data/$SLURM_ARRAY_TASK_ID
pwd

# Run the little boxes simulation
/nesi/project/uoa03404/masters/tau/$DIRECTORY/data/$SLURM_ARRAY_TASK_ID/$FILE_TO_RUN

