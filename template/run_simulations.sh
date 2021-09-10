#!/bin/bash -e
echo $SLURM_ARRAY_TASK_ID
DIRECTORY="working9"
cd /nesi/project/uoa03404/work/$DIRECTORY/data/$SLURM_ARRAY_TASK_ID
pwd

# Run the little boxes simulation
/nesi/project/uoa03404/work/$DIRECTORY/data/$SLURM_ARRAY_TASK_ID/LIBOQF

# Run python scripts here to collect data 