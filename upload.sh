#!/bin/bash

destination="Omega_10_tau_02_phi_pi"

send_up () {
    scp -r template/$1 mahuika:/nesi/project/uoa03404/work/$destination/$1
}

send_up_Little_Boxes () {
    scp Little_Boxes.f08 mahuika:/nesi/project/uoa03404/work/$destination/Little_Boxes.f08
}

send_up python_scripts
send_up summarise.run 
send_up run_simulations.sh 
send_up LIBOQF_array.run 
send_up initialise.run 
send_up_Little_Boxes
