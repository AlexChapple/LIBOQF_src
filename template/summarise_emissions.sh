#!/bin/bash 
#SBATCH --job-name=LIBOQF_summarise_emission
#SBATCH --time=00:30:00
#SBATCH --account=uoa03404
#SBATCH --mem-per-cpu=500

module load Python 
python python_scripts/summarise_emissions.py 